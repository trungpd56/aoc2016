import requests
import os
from pathlib import Path

day = 14
cookies = {"session": os.environ["AOC_SESSION"]}

# Download input
r = requests.get(f"https://adventofcode.com/2016/day/{day}/input", cookies=cookies)
Path(f"input{day:02d}.txt").write_text(r.text)

# Create Sample
pysample = f"""\
#!/usr/bin/env python3

from pathlib import Path







lines = Path(Path(__file__).parent / "input{day:02d}.txt").read_text().strip()


part1 = ""
print(f"Part 1: {{part1}}")
part2 = ""
print(f"Part 2: {{part2}}")


"""
filepy = Path(f"{day:02d}.py")
if not filepy.exists():
    filepy.write_text(pysample)
