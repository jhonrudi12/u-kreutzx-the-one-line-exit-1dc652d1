"""The One-Line Exit (make.fun).

Writes a single funny one-line resignation letter to entry.txt.
The program is deterministic, uses no network, and reads nothing
outside this repository.
"""

import os

ENTRY = "I hereby resign, effective immediately: I have booked my exit interview with the elevator, the only thing here that ever lifted me up."


def check(line: str) -> None:
    """Enforce the competition gate: 1-140 chars, one line, no padding."""
    if not 1 <= len(line) <= 140:
        raise ValueError(f"entry must be 1-140 characters, got {len(line)}")
    if "\n" in line or "\r" in line:
        raise ValueError("entry must be exactly one line")
    if line != line.strip():
        raise ValueError("entry must not start or end with whitespace")


def main() -> None:
    check(ENTRY)
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
