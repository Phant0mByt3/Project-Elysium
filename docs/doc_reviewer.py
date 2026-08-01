#!/usr/bin/env python3
"""
create_docs.py
================
Project Elysium - Documentation Structure Generator

Reads `structure.json` and creates the corresponding folder/file tree on
disk (relative to this script's location, default root: "docs/").

Design goals
------------
- SAFE: never deletes, renames, or overwrites body content. Existing
  folders are always skipped. For existing Markdown files, only the
  title line (the first "# ..." heading) is checked and corrected if
  it doesn't match the expected format, and any broken Markdown links
  inside the file are repointed to the correct target — everything
  else in the file (any notes/content already written) is left
  untouched.
- CONTENT-AGNOSTIC: this script has zero knowledge of what the docs are
  about. All content (folder names, file names) lives in structure.json.
  That means updating the documentation tree never requires touching
  Python code.
- SCALABLE: works the same whether structure.json describes 20 files or
  20,000. Folder creation is idempotent (via os.makedirs(exist_ok=True)
  guarded by an existence check so we can print [SKIPPED] correctly),
  and file creation only ever *adds* new files.

--------------------------------------------------------------------------
HOW TO ADD NEW FOLDERS OR FILES
--------------------------------------------------------------------------
Everything is driven by structure.json. You do NOT need to edit this
script to add new documentation.

1. To add a new FILE to an existing folder:
   Open structure.json, find the folder's "files" list, and append the
   new filename at the END of the list (after the existing numbers).
   Example:
       "files": [
           "0000-Overview.md",
           "0001-Vision.md",
           "0010-New-Topic.md"   <-- new file, new/next free number
       ]

2. To add a new top-level FOLDER:
   Add a new object to the root "folders" array:
       {
           "name": "2100-New-Category",
           "files": ["2100-New-Category.md"],
           "folders": []
       }

3. To add a NESTED sub-folder inside an existing folder:
   Add an entry to that folder's own "folders" array (folders can nest
   to any depth):
       {
           "name": "0100-World",
           "files": [...],
           "folders": [
               {
                   "name": "0100-Subzone",
                   "files": ["0100-Subzone-Overview.md"],
                   "folders": []
               }
           ]
       }

--------------------------------------------------------------------------
LINK CHECKING
--------------------------------------------------------------------------
After the folder/file tree is built, the script scans every Markdown
file in `docs/` for internal links of the form:

    [Some Text](path/to/file.md)

For each one it checks whether that path actually resolves to a real
file on disk (relative to the file containing the link). If it does,
the link is left alone. If it doesn't (the file was renamed, moved, or
the path was simply mistyped), the script looks for a file elsewhere
in the tree with a matching or close-matching filename and rewrites
the link's path to point at it -- the link text and everything else on
that line is left untouched.

- Exactly one plausible match found  -> [LINK FIXED]
- No matching filename anywhere      -> [LINK BROKEN] (left as-is, for
                                          a human to look at)
- More than one equally plausible
  match (duplicate filenames)        -> [LINK AMBIGUOUS] (left as-is)

External links (http://, https://, mailto:) are never touched.

--------------------------------------------------------------------------
EMPTY FILE SUMMARY
--------------------------------------------------------------------------
At the very end of a run, the script walks the whole tree again and
prints a compact list of every Markdown file whose content is nothing
but its title (i.e. still just the "Documentation pending." default,
or blank) -- a quick way to see what's left to write. This is purely
informational and never modifies any file.

--------------------------------------------------------------------------
CONSOLE COLORS
--------------------------------------------------------------------------
    white   [SKIPPED]         nothing needed to change
    green   [FOLDER CREATED]  \
            [FILE CREATED]     > successful, automatic actions
            [TITLE FIXED]     /
            [LINK FIXED]     /
    yellow  [LINK AMBIGUOUS]  multiple possible fixes -- needs a human
    red     [LINK BROKEN]     no fix found -- needs a human
    cyan    [EMPTY]           informational summary, not an action

Set the NO_COLOR environment variable to disable colored output.

--------------------------------------------------------------------------
IMPORTANT RULES (do not break these when editing structure.json)
--------------------------------------------------------------------------
- Never rename or renumber an existing file/folder entry. Numeric
  prefixes are treated as permanent IDs across the life of the project.
- Only ever ADD new entries after the existing ones.
- This script will never overwrite a file/folder that already exists on
  disk, no matter what structure.json says -- it only fills in what is
  missing.
"""

import difflib
import json
import os
import re
import sys

# --------------------------------------------------------------------------
# Configuration
# --------------------------------------------------------------------------

# Default documentation root directory (relative to this script's location).
DEFAULT_DOCS_ROOT = "docs"

# Name of the JSON file describing the documentation tree.
STRUCTURE_FILE = "structure.json"

# Matches Markdown links: [text](target) -- but not images (![...](...)).
_LINK_PATTERN = re.compile(r"(?<!!)\[([^\]\n]*)\]\(([^)\n]+)\)")

# How similar a mistyped filename has to be to an existing one before
# we'll auto-fix it (0.0-1.0, higher = stricter). Avoids "fixing" a
# link into the wrong file just because the names are vaguely similar.
FUZZY_MATCH_CUTOFF = 0.72

# --------------------------------------------------------------------------
# Console colors
# --------------------------------------------------------------------------
# Plain ANSI escape codes -- no external dependencies needed. Sett the
# NO_COLOR environment variable (see https://no-color.org) to turn this
# off, e.g. if you're piping output somewhere that doesn't like escape
# codes.

_USE_COLOR = os.environ.get("NO_COLOR") is None

_ANSI = {
    "white": "\033[37m",
    "green": "\033[32m",
    "yellow": "\033[33m",
    "red": "\033[31m",
    "magenta": "\033[35m",
    "cyan": "\033[36m",
    "reset": "\033[0m",
}

# Color assigned to each status tag:
#   white   - SKIPPED       (nothing needed to change)
#   green   - CREATED/FIXED (a successful, automatic repair)
#   yellow  - AMBIGUOUS     (needs a human to pick)
#   red     - BROKEN        (needs a human to fix)
#   cyan    - EMPTY summary (informational, not an action)
_TAG_COLORS = {
    "FOLDER CREATED": "green",
    "FILE CREATED": "green",
    "SKIPPED": "white",
    "TITLE FIXED": "green",
    "LINK FIXED": "green",
    "LINK BROKEN": "red",
    "LINK AMBIGUOUS": "yellow",
    "EMPTY": "cyan",
    "WARNING": "yellow",
    "ERROR": "red",
}


def tag(label: str) -> str:
    """
    Returns a bracketed, color-coded status tag, e.g. tag("SKIPPED")
    -> "[SKIPPED]" in white. Colors are defined in _TAG_COLORS above.
    Padded to a consistent width so console output lines up in columns.
    """
    color_name = _TAG_COLORS.get(label, "white")
    bracketed = f"[{label}]".ljust(17)

    if not _USE_COLOR:
        return bracketed

    return f"{_ANSI[color_name]}{bracketed}{_ANSI['reset']}"


# --------------------------------------------------------------------------
# Helpers
# --------------------------------------------------------------------------

def expected_heading(filename: str) -> str:
    """
    Computes the exact "# ..." heading line a file should have, based
    on its filename, e.g.:

        1405-Naming-Conventions.md  ->  "# 1405 — Naming Conventions"
        0000-Overview.md            ->  "# 0000 — Overview"
        1500-Expansion-01.md        ->  "# 1500 — Expansion 01"

    Falls back to the bare stem if the filename doesn't follow the
    "<number>-<Words>" pattern.
    """
    stem = os.path.splitext(filename)[0]
    number, sep, rest = stem.partition("-")

    if sep and number.isdigit() and rest:
        words = rest.replace("-", " ")
        heading = f"{number} — {words}"
    else:
        heading = stem

    return f"# {heading}"


def default_markdown_template(filename: str) -> str:
    """
    Returns the default content for a newly created Markdown file,
    using expected_heading() for the title line.
    """
    return f"{expected_heading(filename)}\nDocumentation pending.\n"


def ensure_title_format(path: str, filename: str) -> None:
    """
    Checks an EXISTING Markdown file's first line against the expected
    "# {number} — {Title With Spaces}" heading.

    - If it already matches: does nothing, prints [SKIPPED].
    - If it doesn't match: rewrites ONLY the first line to the correct
      heading. Every other line in the file (body content someone may
      have already written) is left completely untouched.
    """
    wanted = expected_heading(filename)

    with open(path, "r", encoding="utf-8") as f:
        original = f.read()

    first_line, sep, rest = original.partition("\n")

    if first_line == wanted:
        print(f"{tag('SKIPPED')}{path} (title already correct)")
        return

    new_content = wanted + ("\n" + rest if sep else "\n")

    with open(path, "w", encoding="utf-8") as f:
        f.write(new_content)

    print(f"{tag('TITLE FIXED')}{path}")


def create_folder(path: str) -> None:
    """
    Creates `path` if it doesn't already exist. Never touches an
    existing folder. Prints a [FOLDER CREATED] or [SKIPPED] line.
    """
    if os.path.isdir(path):
        print(f"{tag('SKIPPED')}{path} (folder already exists)")
        return

    # exist_ok=True guards against race conditions / already-created
    # parent folders; the isdir() check above is what actually decides
    # whether we report a creation or a skip.
    os.makedirs(path, exist_ok=True)
    print(f"{tag('FOLDER CREATED')}{path}")


def create_markdown_file(path: str) -> None:
    """
    If `path` doesn't exist yet, creates it with the default template.

    If it already exists, its content is NEVER overwritten wholesale —
    but its title line IS checked against the expected format and
    corrected if needed (see ensure_title_format). This is the one
    exception to "never touch existing files": everything except the
    heading line is always preserved untouched.
    """
    filename = os.path.basename(path)

    if os.path.isfile(path):
        ensure_title_format(path, filename)
        return

    content = default_markdown_template(filename)

    with open(path, "w", encoding="utf-8") as f:
        f.write(content)

    print(f"{tag('FILE CREATED')}{path}")


def build_markdown_index(root_path: str) -> dict:
    """
    Walks the whole docs tree and builds an index of every Markdown
    file, keyed by lowercased filename:

        { "0405-naming-conventions.md": ["/abs/path/.../0405-....md"] }

    A list is used per key (rather than a single path) so that if two
    files somehow share a filename in different folders, we can detect
    the ambiguity instead of silently picking one.
    """
    index: dict[str, list[str]] = {}

    for dirpath, _dirnames, filenames in os.walk(root_path):
        for filename in filenames:
            if filename.lower().endswith(".md"):
                key = filename.lower()
                index.setdefault(key, []).append(os.path.join(dirpath, filename))

    return index


def resolve_link_target(basename: str, index: dict) -> list:
    """
    Given the basename of a link target (e.g. "Naming-Conventions.md"),
    tries to find matching real file(s) in `index`:

      1. Exact (case-insensitive) filename match.
      2. If none, a fuzzy match against all known filenames, to catch
         typos (e.g. "Namign-Conventons.md" -> "Naming-Conventions.md").

    Returns a list of absolute paths (empty if nothing plausible was
    found; more than one entry means the match was ambiguous).
    """
    key = basename.lower()

    if key in index:
        return index[key]

    close = difflib.get_close_matches(key, index.keys(), n=3, cutoff=FUZZY_MATCH_CUTOFF)
    matches: list = []
    for candidate_key in close:
        matches.extend(index[candidate_key])
    return matches


def fix_links_in_file(path: str, index: dict) -> None:
    """
    Scans a single Markdown file for [text](target.md) links and
    repoints any that are broken (target doesn't exist relative to
    this file) at the correct file, if exactly one plausible candidate
    can be found in `index`. Leaves everything else in the file byte
    for byte identical. Writes the file back only if a fix was made.
    """
    with open(path, "r", encoding="utf-8") as f:
        original = f.read()

    source_dir = os.path.dirname(path)
    made_changes = {"value": False}

    def repl(match: "re.Match") -> str:
        link_text, target = match.group(1), match.group(2)

        # Never touch external links or anchors-only links.
        if target.startswith(("http://", "https://", "mailto:", "#")):
            return match.group(0)

        target_path, hash_sep, anchor = target.partition("#")

        if not target_path.lower().endswith(".md"):
            return match.group(0)

        resolved = os.path.normpath(os.path.join(source_dir, target_path))
        if os.path.isfile(resolved):
            return match.group(0)  # link is fine as-is

        # Broken link -- try to find where the file actually lives.
        basename = os.path.basename(target_path)
        candidates = resolve_link_target(basename, index)

        if len(candidates) == 1:
            new_rel = os.path.relpath(candidates[0], source_dir).replace(os.sep, "/")
            new_target = new_rel + (("#" + anchor) if hash_sep else "")
            made_changes["value"] = True
            print(f"{tag('LINK FIXED')}{path}\n"
                  f"                 '{target}' -> '{new_target}'")
            return f"[{link_text}]({new_target})"

        elif len(candidates) > 1:
            print(f"{tag('LINK AMBIGUOUS')}{path}\n"
                  f"                 '{target}' matches multiple files, left as-is")
            return match.group(0)

        else:
            print(f"{tag('LINK BROKEN')}{path}\n"
                  f"                 '{target}' -- no matching file found, left as-is")
            return match.group(0)

    updated = _LINK_PATTERN.sub(repl, original)

    if made_changes["value"]:
        with open(path, "w", encoding="utf-8") as f:
            f.write(updated)


def check_all_links(root_path: str) -> None:
    """
    Second pass over the whole docs tree: builds a filename index, then
    checks and fixes internal Markdown links in every .md file found.
    Run after the folder/file structure has been created, so newly
    created files are included too.
    """
    print("\nChecking internal links...")
    index = build_markdown_index(root_path)

    for dirpath, _dirnames, filenames in os.walk(root_path):
        for filename in filenames:
            if filename.lower().endswith(".md"):
                fix_links_in_file(os.path.join(dirpath, filename), index)


def is_placeholder_only(content: str) -> bool:
    """
    Returns True if `content` is "empty" in the sense that matters for
    documentation: nothing but the title line, optionally followed by
    the default "Documentation pending." placeholder and/or blank
    lines. Any real body content at all makes this False.
    """
    _first_line, _sep, rest = content.partition("\n")
    body = rest.strip()
    return body == "" or body == "Documentation pending."


def find_empty_files(root_path: str) -> list:
    """
    Walks the whole docs tree and returns a sorted list of paths (as
    relative-to-docs-root, forward-slash strings) for every Markdown
    file whose content is nothing but its title (see
    is_placeholder_only). Used to give a compact "these still need
    writing" summary at the end of a run.
    """
    empty_files = []

    for dirpath, _dirnames, filenames in os.walk(root_path):
        for filename in sorted(filenames):
            if not filename.lower().endswith(".md"):
                continue
            full_path = os.path.join(dirpath, filename)
            try:
                with open(full_path, "r", encoding="utf-8") as f:
                    content = f.read()
            except OSError:
                continue
            if is_placeholder_only(content):
                rel = os.path.relpath(full_path, os.path.dirname(root_path))
                empty_files.append(rel.replace(os.sep, "/"))

    return sorted(empty_files)


def report_empty_files(root_path: str) -> None:
    """
    Prints a compact, color-coded list of every Markdown file that
    still contains nothing but its title -- i.e. documentation that
    hasn't been written yet. Purely informational; never modifies
    anything.
    """
    empty_files = find_empty_files(root_path)

    if not empty_files:
        return

    print(f"\n{tag('EMPTY')}{len(empty_files)} file(s) contain nothing but a title "
          f"(documentation still pending):")

    color = _ANSI["cyan"] if _USE_COLOR else ""
    reset = _ANSI["reset"] if _USE_COLOR else ""
    for rel_path in empty_files:
        print(f"{color}  - {rel_path}{reset}")


def process_folder(node: dict, parent_path: str) -> None:
    """
    Recursively processes a folder node from structure.json:
      1. Creates the folder itself.
      2. Creates any Markdown files listed directly inside it.
      3. Recurses into any nested sub-folders.

    `node` is expected to look like:
        {
            "name": "0100-World",
            "files": ["0100-World.md", ...],
            "folders": [ ... nested folder nodes ... ]
        }
    """
    name = node.get("name")
    if not name:
        print(f"{tag('WARNING')}Skipping folder entry with no 'name' field.", file=sys.stderr)
        return

    folder_path = os.path.join(parent_path, name)
    create_folder(folder_path)

    for filename in node.get("files", []):
        file_path = os.path.join(folder_path, filename)
        create_markdown_file(file_path)

    for subfolder in node.get("folders", []):
        process_folder(subfolder, folder_path)


def load_structure(structure_file: str) -> dict:
    """
    Loads and returns the JSON structure describing the documentation
    tree. Exits with a clear error message if the file is missing or
    malformed.
    """
    if not os.path.isfile(structure_file):
        print(f"{tag('ERROR')}Could not find '{structure_file}'. "
              f"Make sure it sits next to create_docs.py.", file=sys.stderr)
        sys.exit(1)

    try:
        with open(structure_file, "r", encoding="utf-8") as f:
            return json.load(f)
    except json.JSONDecodeError as e:
        print(f"{tag('ERROR')}'{structure_file}' is not valid JSON: {e}", file=sys.stderr)
        sys.exit(1)


# --------------------------------------------------------------------------
# Entry point
# --------------------------------------------------------------------------

def main() -> None:
    # Resolve paths relative to this script's own location so the tool
    # can be run from anywhere (e.g. `python create_docs.py` from a
    # different working directory) and still find its sibling files.
    script_dir = os.path.dirname(os.path.abspath(__file__))
    structure_path = os.path.join(script_dir, STRUCTURE_FILE)

    structure = load_structure(structure_path)

    # The root folder name in structure.json ("name") is used as the
    # docs directory name. Falls back to DEFAULT_DOCS_ROOT if missing.
    root_name = structure.get("name", DEFAULT_DOCS_ROOT)
    root_path = os.path.join(script_dir, root_name)

    print(f"Project Elysium Documentation Generator")
    print(f"Docs root: {root_path}\n")

    create_folder(root_path)

    for folder_node in structure.get("folders", []):
        process_folder(folder_node, root_path)

    check_all_links(root_path)
    report_empty_files(root_path)

    print("\nDone.")


if __name__ == "__main__":
    main()
