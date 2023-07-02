#!/usr/bin/env python3

from pathlib import Path
from hashlib import md5


def part1(line):
    i = 0
    pw = ""
    while len(pw) < 8:
        h = md5(f"{line}{i}".encode()).hexdigest()
        if h.startswith("00000"):
            pw += h[5]
        i += 1
    return pw


def part2(line):
    i = 0
    pw = [" "] * 8
    while " " in pw:
        h = md5(f"{line}{i}".encode()).hexdigest()
        if h.startswith("00000"):
            pos = h[5]
            if pos in "01234567" and pw[int(pos)] == " ":
                pw[int(pos)] = h[6]
        i += 1
    return "".join(pw)


line = Path(Path(__file__).parent / "input05.txt").read_text().strip()


part1 = part1(line)
print(f"Part 1: {part1}")
part2 = part2(line)
print(f"Part 2: {part2}")
