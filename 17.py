#!/usr/bin/env python3

from pathlib import Path
from hashlib import md5

moves = {
    "U": (0, -1),
    "D": (0, 1),
    "L": (-1, 0),
    "R": (1, 0),
}


def solve(pcode, start=(0, 0), end=(3, 3), p2=False):
    open = "bcdef"
    if start == end:
        return pcode
    x, y = start
    doors = md5(pcode.encode()).hexdigest()[:4]
    path = None
    for i, c in enumerate(doors):
        if c in open:
            dx, dy = moves["UDLR"[i]]
            if 0 <= x + dx < 4 and 0 <= y + dy < 4:
                res = solve(pcode + "UDLR"[i], (x + dx, y + dy), end, p2)
                if res is not None:
                    if path is None:
                        path = res
                    if p2:
                        path = max(path, res, key=len)
                    else:
                        path = min(path, res, key=len)
    return path


line = Path(Path(__file__).parent / "input17.txt").read_text().strip()
pcode = line

part1 = solve(pcode)[len(pcode) :]
print(f"Part 1: {part1}")
part2 = len(solve(pcode, p2=True)) - len(pcode)
print(f"Part 2: {part2}")
