#!/usr/bin/env python3

from pathlib import Path
from hashlib import md5
import re
from functools import cache


@cache
def hash(salt, n, repeat=1):
    value = f"{salt}{n}"
    for _ in range(repeat):
        value = md5(value.encode()).hexdigest()
    return value


def solve(salt, p2=False):
    triplet = re.compile(r"(.)\1\1")
    index = 0
    keys = []
    while len(keys) < 64:
        h = hash(salt, index, 2017 if p2 else 1)
        # Only consider the first such triplet in a hash
        m = triplet.search(h)
        if m:
            # group(1) specify group, group(0) specify all
            quin = m.group(1) * 5
            for i in range(index + 1, index + 1001):
                h2 = hash(salt, i, 2017 if p2 else 1)
                if quin in h2:
                    keys.append(h)
                    break
        index += 1
    return index - 1


line = Path(Path(__file__).parent / "input14.txt").read_text().strip()
salt = line

part1 = solve(salt)
print(f"Part 1: {part1}")
part2 = solve(salt, True)
print(f"Part 2: {part2}")
