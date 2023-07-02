#!/usr/bin/env python3

from pathlib import Path


def gen_data(data, length):
    while len(data) < length:
        data = data + "0" + "".join("0" if c == "1" else "1" for c in data[::-1])
    return data[:length]


def checksum(data):
    while len(data) % 2 == 0:
        data = "".join("1" if a == b else "0" for a, b in zip(data[::2], data[1::2]))
    return data


lines = Path(Path(__file__).parent / "input16.txt").read_text().strip()


part1 = checksum(gen_data(lines, 272))
print(f"Part 1: {part1}")
part2 = checksum(gen_data(lines, 35651584))
print(f"Part 2: {part2}")
