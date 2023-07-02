#!/usr/bin/env python3

from pathlib import Path
from collections import defaultdict, deque


def is_wall(x, y, fav):
    return bin(x * x + 3 * x + 2 * x * y + y + y * y + fav).count("1") % 2 == 1


def create_map(num, fav):
    grid = defaultdict(lambda: ".")
    for x in range(num):
        for y in range(num):
            if is_wall(x, y, fav):
                grid[(x, y)] = "#"
    return grid


def path(grid, start, end, p2=False):
    queue = deque([(start, 0)])
    seen = set()
    while queue:
        pos, steps = queue.popleft()
        if pos == end:
            return steps
        seen.add(pos)
        if steps == 50 and p2:
            return len(seen)
        for dx, dy in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            new_pos = (pos[0] + dx, pos[1] + dy)
            if (
                new_pos not in seen
                and grid[new_pos] != "#"
                and new_pos[0] >= 0
                and new_pos[1] >= 0
            ):
                queue.append((new_pos, steps + 1))


line = Path(Path(__file__).parent / "input13.txt").read_text().strip()
fav = int(line)

grid = create_map(50, fav)
part1 = path(grid, (1, 1), (31, 39))
print(f"Part 1: {part1}")

part2 = path(grid, (1, 1), (31, 39), True)
print(f"Part 2: {part2}")
