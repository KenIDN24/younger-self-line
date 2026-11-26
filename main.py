#!/usr/bin/env python3
"""One Line to Your Younger Self — make.fun entry.

Writes the single line to /output/entry.txt, byte-for-byte, no trailing
newline. Stdlib only, no network.
"""

import os

LINE = "Ask Dad about the war while it's still a conversation and not a eulogy."

# Sealed gate for this contest: entry.txt must be UTF-8 text of 1 to 200
# characters, a single line, and one sentence.
MIN_LEN = 1
MAX_LEN = 200


def main() -> None:
    data = LINE.encode("utf-8")
    assert MIN_LEN <= len(LINE) <= MAX_LEN, f"line length {len(LINE)} outside sealed gate"
    assert LINE == LINE.strip(), "line must not have surrounding whitespace"
    assert "\n" not in LINE, "entry must be a single line"
    assert LINE.count(".") == 1 and LINE.endswith("."), "entry must be exactly one sentence"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "wb") as f:
        f.write(data)
    # Read-back verification: the file on disk must be byte-identical to
    # the line we intended to submit.
    with open("/output/entry.txt", "rb") as f:
        written = f.read()
    assert written == data, "read-back mismatch: entry.txt differs from LINE"
    assert len(written) == 71, f"expected 71 bytes, got {len(written)}"


if __name__ == "__main__":
    main()
