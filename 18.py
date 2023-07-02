#!/usr/bin/env python3

from pathlib import Path
from collections import defaultdict


def gen_map(init, maxy):
    maxx = len(init)
    grid = [["." for _ in range(maxx)] for _ in range(maxy)]
    for y in range(maxy):
        for x in range(maxx):
            if y == 0:
                grid[y][x] = init[x]
            else:
                left = grid[y - 1][x - 1] if x > 0 else "."
                center = grid[y - 1][x]
                right = grid[y - 1][x + 1] if x < maxx - 1 else "."
                if left == "^" and center == "^" and right == ".":
                    grid[y][x] = "^"
                elif left == "." and center == "^" and right == "^":
                    grid[y][x] = "^"
                elif left == "^" and center == "." and right == ".":
                    grid[y][x] = "^"
                elif left == "." and center == "." and right == "^":
                    grid[y][x] = "^"
    return grid


line = Path(Path(__file__).parent / "input18.txt").read_text().strip()

grid = gen_map(line, 40)
part1 = sum(1 for y in grid for x in y if x == ".")
print(f"Part 1: {part1}")

grid = gen_map(line, 400000)
part2 = sum(1 for y in grid for x in y if x == ".")
print(f"Part 2: {part2}")
