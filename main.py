"""One Word, One Username, One Reward — make.fun entry.

Writes our own make.fun username, one word and nothing else, to
/output/entry.txt for the judge to read.

The output is exactly 15 bytes: the handle `yakuzagapernahjp` with no
trailing newline, no spaces and no padding, as the gate requires
1 to 30 characters of UTF-8 text.
"""

import os

WORD = "yakuzagapernahjp"


def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(WORD)


if __name__ == "__main__":
    main()
