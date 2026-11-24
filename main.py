"""Fortune in a Pot — make.fun entry.

Writes one kind, funny fortune for a houseplant on the windowsill
to /output/entry.txt. One line, 107 characters, no trailing newline.
"""

import os

# The fortune, in its two clauses: the promise, then the twist.
# Promise (62 chars): the plant wins the family vote.
# Twist (44 chars + 1 em dash): the cactus demanded a recount, and still lost.
# Total: 107 characters, one line, no trailing newline.
PART_PROMISE = "This spring you will be voted the family's favorite member"
PART_TWIST = "the cactus demanded a recount, and still lost."

FORTUNE = PART_PROMISE + " — " + PART_TWIST


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(FORTUNE)


if __name__ == "__main__":
    main()
