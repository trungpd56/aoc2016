#!/usr/bin/env python3

from pathlib import Path


class Console:
    def __init__(self, lines, init=0):
        self.lines = lines
        self.r = {"a": 0, "b": 0, "c": init, "d": 0}

    def run(self):
        eip = 0
        while eip < len(self.lines):
            toks = self.lines[eip]
            if toks[0] == "cpy":
                value = self.r[toks[1]] if toks[1].isalpha() else int(toks[1])
                self.r[toks[2]] = value
            elif toks[0] == "inc":
                self.r[toks[1]] += 1
            elif toks[0] == "dec":
                self.r[toks[1]] -= 1
            elif toks[0] == "jnz":
                value1 = self.r[toks[1]] if toks[1].isalpha() else int(toks[1])
                value2 = self.r[toks[2]] if toks[2].isalpha() else int(toks[2])
                if value1 != 0:
                    eip += value2
                    continue
            eip += 1
        return self.r["a"]


lines = Path(Path(__file__).parent / "input12.txt").read_text().strip()
lines = [line.split() for line in lines.splitlines()]

console = Console(lines)
part1 = console.run()
print(f"Part 1: {part1}")

console = Console(lines, 1)
part2 = console.run()
print(f"Part 2: {part2}")
