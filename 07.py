#!/usr/bin/env python3

from pathlib import Path
import re


class Ip:
    def __init__(self, line):
        r_in = re.compile(r"\[(.*?)\]")
        self.hypernets = []

        def rep(m):
            self.hypernets.append(m.group(1))
            return "-"

        self.supernet = re.sub(r_in, rep, line)

    def tls(self):
        r_abba = re.compile(r"(.)(?!\1)(.)\2\1")
        if any(r_abba.search(s) for s in self.hypernets):
            return False
        return True if r_abba.search(self.supernet) else False

    def ssl(self):
        r_aba = re.compile(r"(.)(?!\1)(.)\1")
        i = 0
        abas = []
        # You need to use a while loop here because re.search() will not find overlapping matches
        while found := r_aba.search(self.supernet, i):
            abas.append(found.groups())
            i = found.start() + 1

        babs = [f"{a[1]}{a[0]}{a[1]}" for a in abas]
        return any(bab in h for bab in babs for h in self.hypernets)


lines = Path(Path(__file__).parent / "input07.txt").read_text().strip()
data = lines.splitlines()

part1 = sum(Ip(l).tls() for l in data)
print(f"Part 1: {part1}")
part2 = sum(Ip(l).ssl() for l in data)
print(f"Part 2: {part2}")
