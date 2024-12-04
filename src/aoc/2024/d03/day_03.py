import re
import aoc_helper
from aoc_helper import extract_ints

raw = aoc_helper.fetch(3, 2024)
data = raw


def process_parts(parts):
    return [
        x * y
        for part in parts
        if not part.startswith("n't")
        for expr in re.findall(r"mul\(\d+,\d+\)", part)
        for x, y in [map(int, extract_ints(expr))]
    ]


def group_text(text):
    return sum(process_parts(text.split("do")))


def part_one(data=data):
    return sum(
        int(x) * int(y)
        for expr in re.findall(r"mul\(\d+,\d+\)", data)
        for x, y in [extract_ints(expr)]
    )


def part_two(data=data):
    parts = data.split("do")
    return sum(process_parts([parts[0]]) + process_parts(parts[1:]))


aoc_helper.lazy_test(day=3, year=2024, parse=lambda raw: raw, solution=part_one)
aoc_helper.lazy_test(day=3, year=2024, parse=lambda raw: raw, solution=part_two)

aoc_helper.lazy_submit(day=3, year=2024, solution=part_one, data=data)
aoc_helper.lazy_submit(day=3, year=2024, solution=part_two, data=data)
