#!/usr/bin/env python3

from pathlib import Path
from collections import defaultdict
import math

lines = Path(Path(__file__).parent / "input10.txt").read_text().strip()
init_lines = [line.split() for line in lines.split("\n") if line.startswith("value")]
cmd_lines = [line.split() for line in lines.split("\n") if not line.startswith("value")]

stacks = []
bots = defaultdict(list)
outputs = defaultdict(list)
cmds = defaultdict(list)
for line in init_lines:
    value, bot = int(line[1]), int(line[-1])
    bots[bot].append(value)
    if len(bots[bot]) == 2:
        stacks.append(bot)

for line in cmd_lines:
    if line[0] == "bot":
        bot = int(line[1])
        cmds[bot].extend((line[5], int(line[6]), line[10], int(line[11])))
    else:
        assert False

while stacks:
    name = stacks.pop()
    low, high = sorted(bots[name])
    if low == 17 and high == 61:
        part1 = name
    low_name, low_num, high_name, high_num = cmds[name]
    if low_name == "bot":
        bots[low_num].append(low)
        if len(bots[low_num]) == 2:
            stacks.append(low_num)
    else:
        outputs[low_num].append(low)
    if high_name == "bot":
        bots[high_num].append(high)
        if len(bots[high_num]) == 2:
            stacks.append(high_num)
    else:
        outputs[high_num].append(high)


print(f"Part 1: {part1}")
part2 = math.prod(outputs[i][0] for i in range(3))
print(f"Part 2: {part2}")
