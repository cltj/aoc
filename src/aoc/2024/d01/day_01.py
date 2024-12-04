from collections import Counter
import aoc_helper
from aoc_helper import extract_ints

raw = aoc_helper.fetch(1, 2024)
data = extract_ints(raw)


def separate_list(data: list[int]) -> tuple[list[int], list[int]]:
    return sorted(data[::2]), sorted(data[1::2])


def part_one(data: list[int]) -> int:
    left_list, right_list = separate_list(data)
    return sum(abs(left - right) for left, right in zip(left_list, right_list))


def part_two(data: list[int]) -> int:
    left_list, right_list = separate_list(data)
    right_counter = Counter(right_list)
    return sum(left * right_counter[left] for left in left_list)


aoc_helper.lazy_test(day=1, year=2024, parse=extract_ints, solution=part_one)
aoc_helper.lazy_test(day=1, year=2024, parse=extract_ints, solution=part_two)

aoc_helper.lazy_submit(day=1, year=2024, solution=part_one, data=data)
aoc_helper.lazy_submit(day=1, year=2024, solution=part_two, data=data)
