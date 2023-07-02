#!/usr/bin/env python3

from pathlib import Path
import re


def solve(line, p2=False):
    r = re.compile(r"\((\d+)x(\d+)\)")
    match = r.search(line)
    if match is None:
        return len(line)
    length = 0
    l, n = map(int, match.groups())
    start = match.start()
    end = match.end()
    if not p2:
        length += start + l * n + solve(line[end + l :])
    elif p2:
        length += (
            start + solve(line[end : end + l], True) * n + solve(line[end + l :], True)
        )

    return length


lines = Path(Path(__file__).parent / "input09.txt").read_text().strip()
data = lines.splitlines()


part1 = sum(solve(line) for line in data)
print(f"Part 1: {part1}")
part2 = sum(solve(line, p2=True) for line in data)
print(f"Part 2: {part2}")
