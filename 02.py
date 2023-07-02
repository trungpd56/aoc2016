#!/usr/bin/env python3

from pathlib import Path

dirs = {
    "U": (0, -1),
    "R": (1, 0),
    "D": (0, 1),
    "L": (-1, 0),
}


def part1(data):
    """Solve part 1."""
    kp1 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    code = ""
    x, y = 1, 1
    for line in data:
        for c in line:
            dx, dy = dirs[c]
            x = max(0, min(x + dx, 2))
            y = max(0, min(y + dy, 2))
        code += str(kp1[y][x])
    return code


def part2(data):
    """Solve part 2."""
    kp2 = [
        [0, 0, 1, 0, 0],
        [0, 2, 3, 4, 0],
        [5, 6, 7, 8, 9],
        [0, "A", "B", "C", 0],
        [0, 0, "D", 0, 0],
    ]
    code = ""
    x, y = 0, 2
    for line in data:
        for c in line:
            dx, dy = dirs[c]
            x = max(0, min(x + dx, 4))
            y = max(0, min(y + dy, 4))
            if kp2[y][x] == 0:
                x -= dx
                y -= dy
        code += str(kp2[y][x])
    return code


lines = Path(Path(__file__).parent / "input02.txt").read_text().strip()
lines = lines.split("\n")

part1 = part1(lines)
print(f"Part 1: {part1}")
part2 = part2(lines)
print(f"Part 2: {part2}")
