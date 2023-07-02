#!/usr/bin/env python3

from pathlib import Path


def part1(data):
    cols = zip(*data)
    return "".join(max(col, key=col.count) for col in cols)


def part2(data):
    cols = zip(*data)
    return "".join(min(col, key=col.count) for col in cols)


lines = Path(Path(__file__).parent / "input06.txt").read_text().strip()
data = lines.splitlines()

part1 = part1(data)
print(f"Part 1: {part1}")
part2 = part2(data)
print(f"Part 2: {part2}")
