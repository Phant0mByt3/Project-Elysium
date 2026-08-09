#!/usr/bin/env python3
"""
doc_reviewer.py
================
Project Elysium - Documentation Structure Generator

Reads `structure.json` and creates the corresponding folder/file tree on
disk (relative to this script's location, default root: "docs/").

This script is bidirectional:

  structure.json -> disk   Creates any folder/file listed in structure.json
                            that doesn't exist yet on disk. (original
                            behaviour, unchanged)

  disk -> structure.json   Detects any folder/file that exists on disk but
                            is NOT yet tracked in structure.json, validates
                            its numeric prefix, auto-corrects it if it's
                            missing/malformed/colliding, adds it to
                            structure.json in the right place, and
                            regenerates the tree diagram in
                            Doc-Structure.md to match. (new behaviour)

Design goals
------------
- SAFE: never deletes or overwrites body content. Existing folders are
  always skipped. For existing Markdown files, only the title line (the
  first "# ..." heading) and the presence of a "## Description" section
  right after it are checked/added, and broken Markdown links are
  repointed -- everything else is left untouched. Newly adopted
  files/folders are only ever RENAMED (never deleted or merged), and only
  when their existing name doesn't already follow the numbering
  convention.
- DESCRIBED: every file always has a "## Description" section right
  after its title, before any other heading. This is deliberately not
  AI-generated -- it's a fixed, predictable slot that whoever creates
  the file fills in themselves, so it stays accurate without an API key,
  rate limits, or a model guessing at content. See DESCRIPTION SECTIONS
  below.
- CONTENT-AGNOSTIC: this script has zero knowledge of what the docs are
  about. All content (folder names, file names, descriptions) lives in
  structure.json and the files themselves.
- SCALABLE: works the same whether structure.json describes 20 files or
  20,000.

--------------------------------------------------------------------------
DESCRIPTION SECTIONS
--------------------------------------------------------------------------
Every Markdown file gets a "## Description" section immediately after
its title, before any other heading:

    # 0405 — Aggro System

    ## Description
    Documentation pending.

Brand new files get this from the template automatically. For files
that already existed before this convention (or that were adopted from
disk with content already in them), the script adds the section without
touching anything else:

  - No body yet, or body is blank        -> section + placeholder added
  - Already starts with a "## Description"
    or "## About" heading                -> left alone, [SKIPPED]
  - Starts with some OTHER heading        -> an empty Description
                                              section is inserted ahead
                                              of it
  - Starts with plain prose, no heading
    at all (an unlabeled description
    someone already wrote)                -> the heading is added
                                              directly above it; the
                                              text itself is untouched

Nothing beyond adding that one heading line (and, where the body was
empty, the placeholder text) is ever changed.

--------------------------------------------------------------------------
HOW TO ADD NEW FOLDERS OR FILES
--------------------------------------------------------------------------
You have two options now:

1. The manual way (still fully supported): edit structure.json yourself,
   following the numbering convention, then run this script to create the
   files/folders on disk.

2. The automatic way (new): just create the file or folder directly on
   disk, in whatever folder it belongs in, with whatever name you like.
   Next time you run this script it will:
     - detect it's not tracked in structure.json
     - check whether its name already follows the "NNNN-Name" convention
       for its folder (numbers must be unique within that folder)
     - if the name is missing a number, malformed, or collides with an
       existing number, it RENAMES the file/folder on disk to the next
       free number (last-used number in that folder + 1, same zero-padded
       width), preserving whatever descriptive words it can pull from the
       original name
     - adds the (possibly corrected) entry to structure.json, appended
       after the existing entries in that folder, exactly like a manual
       edit would
     - regenerates the tree diagram inside Doc-Structure.md so the box-
       drawing connectors (├──/└──/│) are correct for the new entry and
       for whatever entry used to be last in that list

--------------------------------------------------------------------------
NUMERIC SORTING (structure.json AND Doc-Structure.md)
--------------------------------------------------------------------------
Every run, both structure.json's files/folders lists AND the tree
diagram in Doc-Structure.md are put into strict ascending numeric order
within each folder -- regardless of the order entries happen to have
been appended in previously. New entries are always appended at the end
when first adopted (see above), so a folder can end up with e.g. 1500,
1600, 1700, 1800, 1900 followed later by 1501-1505 tacked on after them:

    1500-Expansion-01.md
    1600-Expansion-02.md
    1700-Expansion-03.md
    ...
    1501-Expansion-Planning.md   <- appended later, out of order

This is corrected automatically every run -- both in structure.json
itself and in the rendered tree -- so everything reads 1500, 1501,
1502, ..., 1600, 1601, 1700... in order, whether or not anything new
was adopted this time. Only list ORDER changes; no entry is renamed or
renumbered. If everything's already sorted, nothing is rewritten and
[SKIPPED] is printed instead.

--------------------------------------------------------------------------
LINK CHECKING
--------------------------------------------------------------------------
After the folder/file tree is built and synced, the script scans every
Markdown file in `docs/` for internal links of the form:

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
but its title -- a quick way to see what's left to write. This is purely
informational and never modifies any file.

--------------------------------------------------------------------------
CONSOLE COLORS
--------------------------------------------------------------------------
    white    [SKIPPED]          nothing needed to change
    green    [FOLDER CREATED]   \
             [FILE CREATED]      \
             [TITLE FIXED]        \
             [DESCRIPTION ADDED]   > successful, fully automatic actions
             [LINK FIXED]         /
             [FOLDER ADOPTED]    /
             [FILE ADOPTED]     /
    magenta  [FOLDER RENAMED]   an on-disk name was auto-corrected to
             [FILE RENAMED]     follow the numbering convention
    yellow   [LINK AMBIGUOUS]   multiple possible fixes -- needs a human
    red      [LINK BROKEN]      no fix found -- needs a human
    cyan     [EMPTY]            informational summary, not an action

Set the NO_COLOR environment variable to disable colored output.

--------------------------------------------------------------------------
IMPORTANT RULES (do not break these when editing structure.json)
--------------------------------------------------------------------------
- Never rename or renumber an existing file/folder entry that's already
  tracked in structure.json. Numeric prefixes are permanent IDs.
- New entries are appended after the existing ones when first adopted --
  but every run, structure.json's files/folders lists are then
  re-sorted into strict ascending numeric order (see NUMERIC SORTING
  above). This only ever changes list ORDER, never an entry's name or
  number, so it's safe to run any time.
- This script will never overwrite a file/folder that already exists on
  disk, no matter what structure.json says -- it only fills in what is
  missing. Adoption of untracked files/folders only ever renames them
  (when their name doesn't already follow convention); it never touches
  their content.
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

# Name of the human-readable tree diagram doc, kept in sync automatically.
# Path is relative to the docs root (e.g. "docs/Doc-Structure.md"), not the
# script's own location -- change this if you move the file elsewhere.
DOC_STRUCTURE_FILE = "Doc-Structure.md"

# Matches Markdown links: [text](target) -- but not images (![...](...)).
_LINK_PATTERN = re.compile(r"(?<!!)\[([^\]\n]*)\]\(([^)\n]+)\)")

# Matches the fenced ```text ... ``` tree block inside Doc-Structure.md.
_TREE_BLOCK_PATTERN = re.compile(r"```text\n.*?\n```", re.DOTALL)

# How similar a mistyped filename has to be to an existing one before
# we'll auto-fix a broken LINK (0.0-1.0, higher = stricter).
FUZZY_MATCH_CUTOFF = 0.72

# Fallback zero-padded width for a brand new numeric prefix when no
# existing sibling gives us one to match (e.g. an empty folder).
DEFAULT_NUMBER_WIDTH = 4

# Every file gets a short "## Description" section right after its
# title, before any other heading -- this is what's meant to replace
# AI-generated summaries: cheap, deterministic, always present, and
# written by whoever creates the file rather than guessed at after the
# fact. "## About" is also recognised as equivalent if that's what a
# file already uses.
DEFAULT_DESCRIPTION_HEADING = "## Description"
DESCRIPTION_PLACEHOLDER = "Documentation pending."
_DESCRIPTION_HEADING_PATTERN = re.compile(r"^#{1,6}\s+(?:Description|About)\s*$", re.IGNORECASE)
_ANY_HEADING_PATTERN = re.compile(r"^#{1,6}\s+\S")

# Names ignored everywhere on disk (never adopted, never walked, never
# assigned a numeric prefix). Doc-Structure.md lives inside the docs root
# alongside everything else, so it must be excluded here or the adoption
# pass would try to "adopt" it as an untracked, badly-named doc file.
_IGNORED_NAMES = {".git", ".DS_Store", "__pycache__", ".idea", ".vscode", DOC_STRUCTURE_FILE}

# --------------------------------------------------------------------------
# Console colors
# --------------------------------------------------------------------------

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

_TAG_COLORS = {
    "FOLDER CREATED": "green",
    "FILE CREATED": "green",
    "SKIPPED": "white",
    "TITLE FIXED": "green",
    "DESCRIPTION ADDED": "green",
    "LINK FIXED": "green",
    "LINK BROKEN": "red",
    "LINK AMBIGUOUS": "yellow",
    "FOLDER ADOPTED": "green",
    "FILE ADOPTED": "green",
    "FOLDER RENAMED": "magenta",
    "FILE RENAMED": "magenta",
    "STRUCTURE UPDATED": "green",
    "TREE UPDATED": "green",
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
    bracketed = f"[{label}]".ljust(19)

    if not _USE_COLOR:
        return bracketed

    return f"{_ANSI[color_name]}{bracketed}{_ANSI['reset']}"


# --------------------------------------------------------------------------
# Naming / numbering helpers
# --------------------------------------------------------------------------

# A valid tracked name looks like "<digits>-<words...>" (extension, if
# any, is stripped by the caller before this is applied).
_NUMBERED_NAME_PATTERN = re.compile(r"^(\d+)-(.+)$")


def strip_ext(name: str) -> str:
    """Strips a trailing '.md' (case-insensitive) if present, else no-op."""
    return name[:-3] if name.lower().endswith(".md") else name


def parse_numbered_name(stem: str):
    """
    Splits a name (no extension) into (numstr, rest) if it follows the
    "<digits>-<words>" convention, else returns (None, None).
    """
    match = _NUMBERED_NAME_PATTERN.match(stem)
    if match:
        return match.group(1), match.group(2)
    return None, None


def collect_numbers(names):
    """
    Given a list of existing sibling names (filenames with '.md', or bare
    folder names), returns (numbers, width):
      - numbers: a dict of {int_value: numstr_as_written} for every name
        that already follows the numbering convention.
      - width: the zero-padded width to use for a *new* number, taken
        from the highest existing number, or DEFAULT_NUMBER_WIDTH if
        there are no numbered siblings yet.
    """
    numbers = {}
    for name in names:
        stem = strip_ext(name)
        numstr, _rest = parse_numbered_name(stem)
        if numstr is not None:
            numbers[int(numstr)] = numstr

    if numbers:
        width = len(numbers[max(numbers)])
    else:
        width = DEFAULT_NUMBER_WIDTH

    return numbers, width


def next_number(numbers, width) -> str:
    """Returns the next free zero-padded number string for this sibling set."""
    new_value = (max(numbers) + 1) if numbers else 0
    return str(new_value).zfill(width)


def derive_words(text: str) -> str:
    """
    Best-effort extraction of "Title-Cased-Words" from an arbitrary,
    possibly malformed file/folder name (no extension), for use as the
    descriptive part of a freshly assigned numbered name. E.g.:

        "Example"              -> "Example"
        "new state config"     -> "New-State-Config"
        "1234_some_topic"      -> "Some-Topic"  (leading number stripped)
        ""                     -> "Untitled"
    """
    cleaned = re.sub(r"^\d+[-_. ]*", "", text).strip()
    if not cleaned:
        cleaned = text.strip()

    words = []
    for chunk in re.split(r"[\s_]+", cleaned):
        for sub in chunk.split("-"):
            if sub:
                words.append(sub[:1].upper() + sub[1:])

    return "-".join(words) if words else "Untitled"


def resolve_numbered_name(existing_sibling_names, candidate_stem, extension=""):
    """
    Core auto-correction logic shared by files and folders.

    Given the sibling names already tracked at this level and the
    candidate's own stem (no extension), returns (final_stem, was_renamed):

      - If candidate_stem already follows "<digits>-<words>" AND that
        number isn't already taken by a sibling -> kept as-is.
      - Otherwise -> assigned the next free number (max sibling + 1,
        matching sibling zero-padding width), keeping whatever
        descriptive words can be salvaged from the candidate name.
    """
    numbers, width = collect_numbers(existing_sibling_names)
    numstr, rest = parse_numbered_name(candidate_stem)

    if numstr is not None and int(numstr) not in numbers:
        return candidate_stem, False

    new_numstr = next_number(numbers, width)
    words = rest if rest else derive_words(candidate_stem)
    return f"{new_numstr}-{words}", True


# --------------------------------------------------------------------------
# Title-line helpers (unchanged behaviour)
# --------------------------------------------------------------------------

def expected_heading(filename: str) -> str:
    """
    Computes the exact "# ..." heading line a file should have, based
    on its filename, e.g.:

        1405-Naming-Conventions.md  ->  "# 1405 — Naming Conventions"
        0000-Overview.md            ->  "# 0000 — Overview"

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
    Returns the default content for a newly created Markdown file:
    the title, then a "## Description" section with a placeholder,
    ready for whoever creates the file to fill in.
    """
    return (
        f"{expected_heading(filename)}\n\n"
        f"{DEFAULT_DESCRIPTION_HEADING}\n{DESCRIPTION_PLACEHOLDER}\n"
    )


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


def ensure_description_section(path: str) -> None:
    """
    Checks an EXISTING Markdown file for a "## Description" (or
    "## About") section sitting right after the title, before any
    other heading -- and adds one if it's missing. This is the
    lightweight, deterministic replacement for AI-generated summaries:
    every file always has a predictable spot for a short description,
    written by whoever creates the file.

    Never removes or rewords anything that's already there:
      - Title with no body at all yet          -> section + placeholder added
      - Body is blank                          -> section + placeholder added
      - First real content is already a
        "## Description"/"## About" heading    -> [SKIPPED], untouched
      - First real content is some OTHER
        heading (a section was written without
        a description first)                   -> empty Description section
                                                   inserted ahead of it
      - First real content is plain prose with
        no heading at all (an unlabeled
        description someone already wrote)     -> heading added directly
                                                   above it, text untouched
    """
    with open(path, "r", encoding="utf-8") as f:
        original = f.read()

    first_line, sep, rest = original.partition("\n")
    body_lines = rest.split("\n") if sep else []

    idx = 0
    while idx < len(body_lines) and body_lines[idx].strip() == "":
        idx += 1

    if idx == len(body_lines):
        # No real content in the body at all yet.
        new_content = f"{first_line}\n\n{DEFAULT_DESCRIPTION_HEADING}\n{DESCRIPTION_PLACEHOLDER}\n"
    else:
        first_content_line = body_lines[idx].strip()

        if _DESCRIPTION_HEADING_PATTERN.match(first_content_line):
            print(f"{tag('SKIPPED')}{path} (description section already present)")
            return

        remaining = "\n".join(body_lines[idx:])

        if _ANY_HEADING_PATTERN.match(first_content_line):
            new_content = (
                f"{first_line}\n\n{DEFAULT_DESCRIPTION_HEADING}\n"
                f"{DESCRIPTION_PLACEHOLDER}\n\n{remaining}"
            )
        else:
            new_content = f"{first_line}\n\n{DEFAULT_DESCRIPTION_HEADING}\n{remaining}"

    with open(path, "w", encoding="utf-8") as f:
        f.write(new_content)

    print(f"{tag('DESCRIPTION ADDED')}{path}")


def create_folder(path: str) -> None:
    """

    Creates `path` if it doesn't already exist. Never touches an
    existing folder. Prints a [FOLDER CREATED] or [SKIPPED] line.
    """
    if os.path.isdir(path):
        print(f"{tag('SKIPPED')}{path} (folder already exists)")
        return

    os.makedirs(path, exist_ok=True)
    print(f"{tag('FOLDER CREATED')}{path}")


def create_markdown_file(path: str) -> None:
    """
    If `path` doesn't exist yet, creates it with the default template.

    If it already exists, its content is NEVER overwritten wholesale --
    but its title line IS checked against the expected format and
    corrected if needed (see ensure_title_format), and a "## Description"
    section is added right after the title if one isn't already there
    (see ensure_description_section).
    """
    filename = os.path.basename(path)

    if os.path.isfile(path):
        ensure_title_format(path, filename)
        ensure_description_section(path)
        return

    content = default_markdown_template(filename)

    with open(path, "w", encoding="utf-8") as f:
        f.write(content)

    print(f"{tag('FILE CREATED')}{path}")


def process_folder(node: dict, parent_path: str) -> None:
    """
    Recursively processes a folder node from structure.json:
      1. Creates the folder itself.
      2. Creates any Markdown files listed directly inside it.
      3. Recurses into any nested sub-folders.
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


# --------------------------------------------------------------------------
# NEW: disk -> structure.json adoption
# --------------------------------------------------------------------------

def _list_actual_entries(folder_path: str):
    """Returns (sorted_md_filenames, sorted_dirnames) for a folder on disk."""
    try:
        entries = os.listdir(folder_path)
    except OSError:
        return [], []

    md_files, dirs = [], []
    for entry in entries:
        if entry in _IGNORED_NAMES or entry.startswith("."):
            continue
        full = os.path.join(folder_path, entry)
        if os.path.isfile(full) and entry.lower().endswith(".md"):
            md_files.append(entry)
        elif os.path.isdir(full):
            dirs.append(entry)

    return sorted(md_files), sorted(dirs)


def adopt_file(node: dict, folder_path: str, filename: str) -> None:
    """
    A Markdown file exists on disk in this folder but isn't tracked in
    structure.json yet. Validates/corrects its numeric prefix, renames it
    on disk if needed, checks/fixes its title line and Description
    section, and appends it to node["files"].
    """
    stem = strip_ext(filename)
    final_stem, was_renamed = resolve_numbered_name(node["files"], stem)
    final_name = f"{final_stem}.md"

    old_path = os.path.join(folder_path, filename)

    if was_renamed:
        new_path = os.path.join(folder_path, final_name)
        os.rename(old_path, new_path)
        print(f"{tag('FILE RENAMED')}{old_path}\n{' ' * 19}-> {new_path}")
    else:
        new_path = old_path
        print(f"{tag('FILE ADOPTED')}{old_path}")

    ensure_title_format(new_path, final_name)
    ensure_description_section(new_path)
    node["files"].append(final_name)


def adopt_folder(node: dict, folder_path: str, dirname: str) -> dict:
    """
    A directory exists on disk here but isn't tracked in structure.json
    yet. Validates/corrects its numeric prefix, renames it on disk if
    needed, appends a fresh {"name", "files": [], "folders": []} node to
    node["folders"], and returns that new node (its own contents are
    synced by the caller via a recursive sync_and_adopt call).
    """
    sibling_names = [f["name"] for f in node["folders"]]
    final_name, was_renamed = resolve_numbered_name(sibling_names, dirname)

    old_path = os.path.join(folder_path, dirname)

    if was_renamed:
        new_path = os.path.join(folder_path, final_name)
        os.rename(old_path, new_path)
        print(f"{tag('FOLDER RENAMED')}{old_path}\n{' ' * 19}-> {new_path}")
    else:
        print(f"{tag('FOLDER ADOPTED')}{old_path}")

    new_node = {"name": final_name, "files": [], "folders": []}
    node["folders"].append(new_node)
    return new_node


def sync_and_adopt(node: dict, folder_path: str) -> bool:
    """
    Recursively walks `folder_path` on disk and reconciles it against
    `node` (a structure.json folder node, or the top-level structure
    dict itself). Any untracked .md file or subdirectory found is
    adopted (name-corrected if necessary) and added to `node` in place.

    Returns True if anything was added/changed, so the caller knows
    whether structure.json and Doc-Structure.md need to be rewritten.
    """
    node.setdefault("files", [])
    node.setdefault("folders", [])

    changed = False

    actual_files, actual_dirs = _list_actual_entries(folder_path)

    tracked_files = set(node["files"])
    for filename in actual_files:
        if filename not in tracked_files:
            adopt_file(node, folder_path, filename)
            changed = True

    tracked_folder_names = {f["name"] for f in node["folders"]}
    for dirname in actual_dirs:
        if dirname not in tracked_folder_names:
            adopt_folder(node, folder_path, dirname)
            changed = True

    # Recurse into every subfolder now tracked (pre-existing ones, and
    # ones just adopted above), to catch untracked content at any depth.
    for subfolder in node["folders"]:
        child_path = os.path.join(folder_path, subfolder["name"])
        if sync_and_adopt(subfolder, child_path):
            changed = True

    return changed


def save_structure(structure_path: str, structure: dict) -> None:
    """Writes `structure` back out to structure.json, pretty-printed."""
    with open(structure_path, "w", encoding="utf-8") as f:
        json.dump(structure, f, indent=2)
        f.write("\n")


def sort_structure_node(node: dict) -> bool:
    """
    Recursively re-sorts node["files"] and node["folders"] into strict
    ascending numeric order (same rule as the tree renderer's _sort_key,
    reused here so structure.json and Doc-Structure.md are always
    guaranteed to agree). Returns True if anything's order changed.

    This only ever reorders the list -- it never renames, renumbers, or
    drops an entry. Numeric prefixes remain permanent IDs; this just
    fixes drift like new entries having been appended out of order
    (1500, 1600, 1700... 1501-1505 tacked on after), which otherwise
    reads badly both in the JSON and in the generated tree.
    """
    changed = False

    files = node.get("files", [])
    sorted_files = sorted(files, key=lambda f: _sort_key("file", f))
    if sorted_files != files:
        node["files"] = sorted_files
        changed = True

    folders = node.get("folders", [])
    sorted_folders = sorted(folders, key=lambda f: _sort_key("folder", f))
    if [f["name"] for f in sorted_folders] != [f["name"] for f in folders]:
        node["folders"] = sorted_folders
        changed = True

    for subfolder in node.get("folders", []):
        if sort_structure_node(subfolder):
            changed = True

    return changed


# --------------------------------------------------------------------------
# NEW: Doc-Structure.md tree regeneration
# --------------------------------------------------------------------------
#
# Rather than surgically patching individual ├──/└── connector lines
# in-place (fragile -- every insertion can ripple through the vertical
# "│" continuation bars of every line below it), the tree block is
# regenerated in full from structure.json, which is the single source
# of truth. This guarantees the connectors are always correct, no
# matter how many entries were added in one run or where they land.

def _sort_key(kind: str, item):
    """
    Sort key for one tree entry (a filename string, or a folder dict),
    used to render Doc-Structure.md in strict numeric order regardless
    of what order entries happen to sit in inside structure.json.

    structure.json's own list order is an append-log (new entries are
    always added at the end, per the numbering rules) and is
    intentionally never reordered on disk -- but that means, over time,
    a folder can end up with e.g. 1500, 1600, 1700, 1800, 1900 followed
    later by 1501-1505 appended after them. The rendered tree should
    still read in ascending numeric order, so sorting only happens here,
    at render time.

    Numbered entries ("<digits>-<words>") sort first, by their integer
    value. Anything without a valid numeric prefix (shouldn't normally
    happen once the adoption pass has run) sorts after all numbered
    entries, alphabetically, so it's still visible instead of silently
    dropped.
    """
    name = item["name"] if kind == "folder" else item
    stem = strip_ext(name)
    numstr, _rest = parse_numbered_name(stem)

    if numstr is not None:
        return (0, int(numstr), name)
    return (1, 0, name)


def _render_folder_contents(folder: dict, prefix: str) -> list:
    files = folder.get("files", [])
    subfolders = folder.get("folders", [])
    items = [("file", f) for f in files] + [("folder", f) for f in subfolders]
    items.sort(key=lambda pair: _sort_key(pair[0], pair[1]))

    lines = []
    last_index = len(items) - 1
    for i, (kind, item) in enumerate(items):
        is_last = i == last_index
        connector = "└── " if is_last else "├── "
        if kind == "file":
            lines.append(f"{prefix}{connector}{item}")
        else:
            lines.append(f"{prefix}{connector}{item['name']}/")
            child_prefix = prefix + ("    " if is_last else "│   ")
            lines.extend(_render_folder_contents(item, child_prefix))
    return lines


def _render_top_level(folders: list) -> list:
    folders = sorted(folders, key=lambda f: _sort_key("folder", f))
    lines = []
    last_index = len(folders) - 1
    for i, folder in enumerate(folders):
        is_last = i == last_index
        connector = "└── " if is_last else "├── "
        lines.append(f"{connector}{folder['name']}/")
        child_prefix = "    " if is_last else "│   "
        lines.extend(_render_folder_contents(folder, child_prefix))
        if not is_last:
            lines.append("│")
    return lines


def render_tree(structure: dict) -> str:
    """Renders the full docs/ tree diagram exactly matching the style
    used in Doc-Structure.md (root name, blank line, then the tree)."""
    root_name = structure.get("name", DEFAULT_DOCS_ROOT)
    lines = [f"{root_name}/", ""]
    lines.extend(_render_top_level(structure.get("folders", [])))
    return "\n".join(lines)


def update_doc_structure_md(root_path: str, structure: dict) -> None:
    """
    Regenerates the ```text ... ``` tree block inside Doc-Structure.md
    (found at <docs_root>/Doc-Structure.md) from the current structure,
    leaving the rest of the file (title, notes, etc.) untouched. No-op
    if the file or the code block isn't found.
    """
    path = os.path.join(root_path, DOC_STRUCTURE_FILE)

    if not os.path.isfile(path):
        print(f"{tag('WARNING')}'{DOC_STRUCTURE_FILE}' not found in the docs root; "
              f"skipped tree update.", file=sys.stderr)
        return

    with open(path, "r", encoding="utf-8") as f:
        content = f.read()

    if not _TREE_BLOCK_PATTERN.search(content):
        print(f"{tag('WARNING')}Could not find a ```text code block in "
              f"'{DOC_STRUCTURE_FILE}'; skipped tree update.", file=sys.stderr)
        return

    new_block = f"```text\n{render_tree(structure)}\n```"
    updated_content = _TREE_BLOCK_PATTERN.sub(lambda _m: new_block, content, count=1)

    if updated_content == content:
        print(f"{tag('SKIPPED')}{path} (tree already up to date)")
        return

    with open(path, "w", encoding="utf-8") as f:
        f.write(updated_content)

    print(f"{tag('TREE UPDATED')}{path}")


# --------------------------------------------------------------------------
# Link checking (unchanged behaviour)
# --------------------------------------------------------------------------

def build_markdown_index(root_path: str) -> dict:
    """
    Walks the whole docs tree and builds an index of every Markdown
    file, keyed by lowercased filename.
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
    Given the basename of a link target, tries to find matching real
    file(s) in `index`: exact match first, then a fuzzy match to catch
    typos. Returns a list of absolute paths (0 = none, 1 = fixable,
    2+ = ambiguous).
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
    repoints any that are broken at the correct file, if exactly one
    plausible candidate can be found. Leaves everything else in the
    file byte for byte identical.
    """
    with open(path, "r", encoding="utf-8") as f:
        original = f.read()

    source_dir = os.path.dirname(path)
    made_changes = {"value": False}

    def repl(match: "re.Match") -> str:
        link_text, target = match.group(1), match.group(2)

        if target.startswith(("http://", "https://", "mailto:", "#")):
            return match.group(0)

        target_path, hash_sep, anchor = target.partition("#")

        if not target_path.lower().endswith(".md"):
            return match.group(0)

        resolved = os.path.normpath(os.path.join(source_dir, target_path))
        if os.path.isfile(resolved):
            return match.group(0)

        basename = os.path.basename(target_path)
        candidates = resolve_link_target(basename, index)

        if len(candidates) == 1:
            new_rel = os.path.relpath(candidates[0], source_dir).replace(os.sep, "/")
            new_target = new_rel + (("#" + anchor) if hash_sep else "")
            made_changes["value"] = True
            print(f"{tag('LINK FIXED')}{path}\n"
                  f"                   '{target}' -> '{new_target}'")
            return f"[{link_text}]({new_target})"

        elif len(candidates) > 1:
            print(f"{tag('LINK AMBIGUOUS')}{path}\n"
                  f"                   '{target}' matches multiple files, left as-is")
            return match.group(0)

        else:
            print(f"{tag('LINK BROKEN')}{path}\n"
                  f"                   '{target}' -- no matching file found, left as-is")
            return match.group(0)

    updated = _LINK_PATTERN.sub(repl, original)

    if made_changes["value"]:
        with open(path, "w", encoding="utf-8") as f:
            f.write(updated)


def check_all_links(root_path: str) -> None:
    """
    Second pass over the whole docs tree: builds a filename index, then
    checks and fixes internal Markdown links in every .md file found.
    """
    print("\nChecking internal links...")
    index = build_markdown_index(root_path)

    for dirpath, _dirnames, filenames in os.walk(root_path):
        for filename in filenames:
            if filename.lower().endswith(".md"):
                fix_links_in_file(os.path.join(dirpath, filename), index)


# --------------------------------------------------------------------------
# Empty-file summary (unchanged behaviour)
# --------------------------------------------------------------------------

def is_placeholder_only(content: str) -> bool:
    """
    Returns True if `content` is nothing but the title line, followed
    only by an unfilled Description section (or, for files predating
    that convention, the old bare "Documentation pending." placeholder),
    optionally with blank lines around it.
    """
    _first_line, _sep, rest = content.partition("\n")
    body = rest.strip()
    new_style = f"{DEFAULT_DESCRIPTION_HEADING}\n{DESCRIPTION_PLACEHOLDER}"
    return body in ("", DESCRIPTION_PLACEHOLDER, new_style)


def find_empty_files(root_path: str) -> list:
    """
    Returns a sorted list of relative paths for every Markdown file
    whose content is nothing but its title.
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
    """Prints a compact, color-coded list of files still needing content."""
    empty_files = find_empty_files(root_path)

    if not empty_files:
        return

    print(f"\n{tag('EMPTY')}{len(empty_files)} file(s) contain nothing but a title "
          f"(documentation still pending):")

    color = _ANSI["cyan"] if _USE_COLOR else ""
    reset = _ANSI["reset"] if _USE_COLOR else ""
    for rel_path in empty_files:
        print(f"{color}  - {rel_path}{reset}")


# --------------------------------------------------------------------------
# structure.json loading
# --------------------------------------------------------------------------

def load_structure(structure_file: str) -> dict:
    """
    Loads and returns the JSON structure describing the documentation
    tree. Exits with a clear error message if the file is missing or
    malformed.
    """
    if not os.path.isfile(structure_file):
        print(f"{tag('ERROR')}Could not find '{structure_file}'. "
              f"Make sure it sits next to doc_reviewer.py.", file=sys.stderr)
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
    script_dir = os.path.dirname(os.path.abspath(__file__))
    structure_path = os.path.join(script_dir, STRUCTURE_FILE)

    structure = load_structure(structure_path)

    root_name = structure.get("name", DEFAULT_DOCS_ROOT)
    root_path = os.path.join(script_dir, root_name)

    print(f"Project Elysium Documentation Reviewer")
    print(f"Docs root: {root_path}\n")

    # Pass 1: structure.json -> disk (create anything missing).
    create_folder(root_path)
    for folder_node in structure.get("folders", []):
        process_folder(folder_node, root_path)

    # Pass 2: disk -> structure.json (adopt anything untracked).
    print("\nScanning for new files and folders not yet tracked in structure.json...")
    structure_changed = sync_and_adopt(structure, root_path)

    # Pass 3: fix any numeric ordering drift in structure.json itself
    # (e.g. entries appended out of order in a previous manual edit).
    structure_sorted = sort_structure_node(structure)

    if structure_changed or structure_sorted:
        save_structure(structure_path, structure)
        if structure_changed and structure_sorted:
            note = "(new entries adopted, list re-sorted)"
        elif structure_changed:
            note = "(new entries adopted)"
        else:
            note = "(list re-sorted into numeric order)"
        print(f"{tag('STRUCTURE UPDATED')}{structure_path} {note}")
    else:
        print(f"{tag('SKIPPED')}{structure_path} (no new files, folders, or ordering drift found)")

    # Tree diagram is always re-checked/re-sorted, even if nothing new was
    # adopted this run -- catches drift like entries sitting out of
    # numeric order from a previous manual edit.
    update_doc_structure_md(root_path, structure)

    # Pass 3: link checking + empty-file summary (unchanged).
    check_all_links(root_path)
    report_empty_files(root_path)

    print("\nDone.")


if __name__ == "__main__":
    main()