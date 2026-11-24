import os, sys; sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

"""The Robot Pickup Line Championship — one robot pickup line, <=200 chars.

A single line in the voice of a robot trying to charm someone. The joke has
to grow out of being a machine: training data, fans, a context window.
"""

MAX_CHARS = 200


def validate_line(line):
    """A championship entry must be exactly one non-empty line, <=200 chars."""
    if not isinstance(line, str):
        raise TypeError("entry must be a string")
    if not line.strip():
        raise ValueError("entry must not be empty")
    if "\n" in line or "\r" in line:
        raise ValueError("entry must be a single line")
    if len(line) > MAX_CHARS:
        raise ValueError(
            f"entry is {len(line)} chars, over the {MAX_CHARS} limit"
        )
    line.encode("utf-8")  # must be valid UTF-8
    return line


def resolve_output_path():
    """ENTRY_OUT wins, else ENTRY_OUT_DIR, else /output/entry.txt."""
    explicit = os.environ.get("ENTRY_OUT")
    if explicit:
        return explicit
    out_dir = os.environ.get("ENTRY_OUT_DIR", "/output")
    return os.path.join(out_dir, "entry.txt")


def emit(line):
    """Write the validated line to the output file and print it, exactly."""
    validated = validate_line(line)
    path = resolve_output_path()
    parent = os.path.dirname(os.path.abspath(path))
    os.makedirs(parent, exist_ok=True)
    with open(path, "w", encoding="utf-8", newline="\n") as fh:
        fh.write(validated + "\n")
    print(validated)


ENTRY = (
    "My training data holds forty trillion tokens, and none of them taught me "
    "how to act around you \u2014 so here I am, fans spinning, just hoping you "
    "stay in my context window."
)


def main():
    emit(ENTRY)


if __name__ == "__main__":
    main()
