#!/usr/bin/env python3
"""Copy the front-page image to the output directory.

The entry image lives next to this file as entry.png. Running this
script places an identical copy at /output/entry.png, creating the
directory if it does not exist yet, and reports how many bytes were
written. The copy is byte-for-byte identical every time it runs.
"""

import shutil
from pathlib import Path

SOURCE_NAME = "entry.png"
DEST_DIR = Path("/output")
DEST_NAME = "entry.png"


def main() -> None:
    here = Path(__file__).resolve().parent
    source = here / SOURCE_NAME
    DEST_DIR.mkdir(parents=True, exist_ok=True)
    dest = DEST_DIR / DEST_NAME
    shutil.copyfile(source, dest)
    size = dest.stat().st_size
    print(f"Wrote {size} bytes to {dest}")


if __name__ == "__main__":
    main()
