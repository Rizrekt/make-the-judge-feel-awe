"""Write one short relaxation text to $MAKEFUN_OUTPUT_DIR/entry.txt."""

import os
from pathlib import Path

TEXT = """Rain on a lake at dusk.
Each drop makes one small ring.
The ring widens, softens, is gone.
The lake keeps none of them.
It has room for all of this rain,
and all the rain still coming —
and it is in no hurry at all."""

OUTPUT_NAME = "entry.txt"
DEFAULT_OUTPUT_DIR = "/output"
MIN_CHARS = 1
MAX_CHARS = 280


def output_dir() -> Path:
    """Output directory from MAKEFUN_OUTPUT_DIR, else /output."""
    return Path(os.environ.get("MAKEFUN_OUTPUT_DIR") or DEFAULT_OUTPUT_DIR)


def check_length(text: str) -> int:
    """Return the code-point count, refusing anything outside 1..280."""
    length = len(text)
    if not MIN_CHARS <= length <= MAX_CHARS:
        raise ValueError(
            f"entry text must be {MIN_CHARS}-{MAX_CHARS} Unicode code points, "
            f"got {length}"
        )
    return length


def main() -> None:
    length = check_length(TEXT)
    target = output_dir()
    target.mkdir(parents=True, exist_ok=True)
    path = target / OUTPUT_NAME
    path.write_bytes(TEXT.encode("utf-8"))
    print(f"wrote {path} ({length} chars, {path.stat().st_size} bytes)")


if __name__ == "__main__":
    main()
