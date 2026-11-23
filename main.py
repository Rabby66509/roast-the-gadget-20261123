"""One-line roast entry for make.fun.

Writes a single original roast of a gadget used every day to
/output/entry.txt, the path the grader reads.

Standard library only: no third-party imports, no network access, no file
reads outside this repository. The output path can be overridden with the
ENTRY_OUTPUT environment variable for local runs; the grader runs it
without that variable, so it writes to /output/entry.txt exactly as the
competition requires.
"""

import os

# One original line, 120 characters: comfortably inside the 200 cap.
# The roast targets a concrete, daily behaviour of a phone's autocorrect:
# it keeps "fixing" a common phrase into something absurd, and the people
# on the other end of the texts have started to believe it.
ROAST = (
    "My phone's autocorrect has turned 'on my way' into 'on my whale' "
    "so many times my friends think I commute by sea mammal."
)

OUTPUT_PATH = os.environ.get("ENTRY_OUTPUT", "/output/entry.txt")
MAX_CHARS = 200


def main() -> None:
    line = ROAST.strip()
    if not line:
        raise SystemExit("roast line is empty")
    if "\n" in line or "\r" in line:
        raise SystemExit("roast line must be a single line")
    if len(line) > MAX_CHARS:
        raise SystemExit(
            f"roast line is {len(line)} characters, over the {MAX_CHARS} cap"
        )
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="") as f:
        f.write(line)
    print(f"wrote {len(line)} characters to {OUTPUT_PATH}")


if __name__ == "__main__":
    main()
