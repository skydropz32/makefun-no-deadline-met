"""Write one single-line joke excusing a missed deadline to /output/entry.txt.

Stdlib only, deterministic, no network: the same line every run.
"""

import os

LINE = "My draft was ready on time, then I proofread it once and it immediately filed for an extension."


def main():
    # The bounty gate: /output/entry.txt must be UTF-8 text of 1 to 200
    # characters, a single line and nothing else. Fail loudly here rather
    # than shipping an invalid entry.
    assert "\n" not in LINE and "\r" not in LINE, "joke must be one line"
    assert 1 <= len(LINE) <= 200, "joke must be 1-200 characters"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="\n") as f:
        f.write(LINE + "\n")


if __name__ == "__main__":
    main()
