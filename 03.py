#!/usr/bin/env python3

from pathlib import Path


def valid(x, y, z):
    x, y, z = sorted([x, y, z])
    return x + y > z


def part1(data):
    """Solve part 1."""
    return sum(valid(*t) for t in data)


def part2(data):
    """Solve part 2."""
    combine = [list(zip(*t)) for t in zip(*[iter(data)]*3)]
    return sum(valid(*t) for c in combine for t in c)


lines = Path(Path(__file__).parent / "input03.txt").read_text().strip()
data = [list(map(int, line.split())) for line in lines.split("\n")]

part1 = part1(data)
print(f"Part 1: {part1}")
part2 = part2(data)
print(f"Part 2: {part2}")


