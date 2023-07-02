#!/usr/bin/env python3

from pathlib import Path
from string import ascii_lowercase as lc


class rooms:
    def __init__(self, line):
        toks = line.split("-")
        self.name = "-".join(toks[:-1])
        self.sector = int(toks[-1].split("[")[0])
        self.checksum = toks[-1].split("[")[1][:-1]

    def valid(self):
        letters = self.name.replace("-", "")
        five = sorted(set(letters), key=lambda x: (-letters.count(x), x))[:5]
        five = "".join(five)
        return five == self.checksum

    def decrypt(self):
        s = self.sector % 26
        tables = str.maketrans(lc + "-", lc[s:] + lc[:s] + " ")
        return self.name.translate(tables)


lines = Path(Path(__file__).parent / "input04.txt").read_text().strip()
data = lines.split("\n")


part1 = sum([rooms(line).sector for line in data if rooms(line).valid()])
print(f"Part 1: {part1}")

valid_room = [rooms(line) for line in data if rooms(line).valid()]
part2 = [room.sector for room in valid_room if "north" in room.decrypt()][0]
print(f"Part 2: {part2}")
