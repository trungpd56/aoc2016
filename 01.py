#!/usr/bin/env python3

from pathlib import Path


dirs = {
    0: (0, 1),
    1: (1, 0),
    2: (0, -1),
    3: (-1, 0),
}


def solve(lines, p2=False):
    x, y, dir = 0, 0, 0
    seen = set()
    for cmd in lines:
        if cmd[0] == "R":
            dir = (dir + 1) % 4
        elif cmd[0] == "L":
            dir = (dir - 1) % 4
        x += dirs[dir][0] * int(cmd[1:])
        y += dirs[dir][1] * int(cmd[1:])
        if (x, y) in seen and p2:
            return abs(x) + abs(y)
        seen.add((x, y))
    return abs(x) + abs(y)


lines = Path(Path(__file__).parent / "input01.txt").read_text()
lines = lines.split(", ")

part1 = solve(lines)
print(f"Part 1: {part1}")
part2 = solve(lines, True)
print(f"Part 2: {part2}")
