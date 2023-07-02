#!/usr/bin/env python3

from pathlib import Path
from itertools import cycle


def solve(n):
    done = set()
    elves = (i for i in cycle(range(1, n + 1)) if i not in done)
    while True:
        for elve in elves:
            if len(done) == n - 1:
                return elve
            done.add(next(elves))


line = Path(Path(__file__).parent / "input19.txt").read_text().strip()


part1 = solve(int(line))
print(f"Part 1: {part1}")
part2 = ""
print(f"Part 2: {part2}")
