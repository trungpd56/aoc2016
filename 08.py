#!/usr/bin/env python3

from pathlib import Path
import re


class Screen:
    def __init__(self, width, height, data):
        self.width = width
        self.height = height
        self.data = data
        self.grid = [[0 for _ in range(width)] for _ in range(height)]

    def run(self):
        for line in data:
            nums = map(int, re.findall(r"\d+", line))
            if line.startswith("rect"):
                w, h = nums
                for y in range(h):
                    for x in range(w):
                        self.grid[y][x] = 1
            elif line.startswith("rotate row"):
                y, n = nums
                self.grid[y] = self.grid[y][-n:] + self.grid[y][:-n]
            elif line.startswith("rotate column"):
                x, n = nums
                col = [self.grid[y][x] for y in range(self.height)]
                col = col[-n:] + col[:-n]
                for y in range(self.height):
                    self.grid[y][x] = col[y]
        return sum(sum(row) for row in self.grid)

    def draw(self):
        for y in range(self.height):
            for x in range(self.width):
                print("#" if self.grid[y][x] else " ", end="")
            print()


lines = Path(Path(__file__).parent / "input08.txt").read_text().strip()
data = lines.splitlines()

screen = Screen(50, 6, data)
part1 = screen.run()
print(f"Part 1: {part1}")
screen.draw()
# print(f"Part 2: {part2}")
