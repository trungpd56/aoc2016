#!/usr/bin/env python3

from pathlib import Path
from collections import defaultdict, deque
import math


class Bot:
    def __init__(self):
        self.high: int = None
        self.low: int = None
        self.ltype: str = None
        self.htype: str = None
        self.chips: list[int] = []

    @property
    def ready(self):
        return len(self.chips) == 2

    def get_chip(self, c: int) -> None:
        if c not in self.chips:
            self.chips = sorted(self.chips + [c])


lines = Path(Path(__file__).parent / "input10.txt").read_text().strip()
bots = defaultdict(Bot)
for line in lines.splitlines():
    t = line.split()
    match t[0]:
        case "value":
            chip, bot = map(int, (t[1], t[-1]))
            bots[bot].get_chip(chip)
        case "bot":
            ltype, htype = t[5], t[-2]
            bot, low, high = map(int, (t[1], t[6], t[-1]))
            bots[bot].ltype = ltype
            bots[bot].htype = htype
            bots[bot].low = low
            bots[bot].high = high

queue = deque(botnum for botnum, bot in bots.items() if bot.ready)
outputs = [None] * 3
targets = [17, 61]
while queue:
    botnum = queue.popleft()
    bot = bots[botnum]
    if not bot.ready:
        continue
    if bot.chips == targets:
        part1 = botnum
    if bot.ltype == "bot":
        bots[bot.low].get_chip(bot.chips[0])
        queue.append(bot.low)
    elif bot.low < 3:
        outputs[bot.low] = bot.chips[0]
    if bot.htype == "bot":
        bots[bot.high].get_chip(bot.chips[1])
        queue.append(bot.high)
    elif bot.high < 3:
        outputs[bot.high] = bot.chips[1]
    if all(o is not None for o in outputs):
        part2 = math.prod(outputs)
        break

print(f"Part 1: {part1}")
print(f"Part 2: {part2}")
