#!/usr/bin/env python3

from pathlib import Path
import re
from collections import defaultdict


lines = Path(Path(__file__).parent / "input15.txt").read_text().strip()
disks = defaultdict(tuple)
disks2 = defaultdict(tuple)
for line in lines.split("\n"):
    name, size, _, pos = map(int, re.findall(r"\d+", line))
    disks[name] = (pos, size)
    disks2[name] = (pos, size)

disks2[7] = (0, 11)

t = 1
p1_done = True
while True:
    if (
        all((pos + t + name) % size == 0 for name, (pos, size) in disks.items())
        and p1_done
    ):
        p1_done = False
        part1 = t
    if all((pos + t + name) % size == 0 for name, (pos, size) in disks2.items()):
        part2 = t
        break
    t += 1


print(f"Part 1: {part1}")
print(f"Part 2: {part2}")
