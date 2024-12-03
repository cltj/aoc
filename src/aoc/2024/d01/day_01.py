from collections import Counter, defaultdict, deque

import aoc_helper
from aoc_helper import (
    Grid,
    PrioQueue,
    SparseGrid,
    decode_text,
    extract_ints,
    extract_iranges,
    extract_ranges,
    extract_uints,
    frange,
    irange,
    iter,
    list,
    map,
    multirange,
    range,
    search,
    tail_call,
)

raw = aoc_helper.fetch(1, 2024)


def parse_raw(raw: str) -> list[int]:
    return extract_ints(raw)


data = parse_raw(raw)


def separate_list(data: list[int]) -> tuple[list[int], list[int]]:
    left_list = data[::2]
    right_list = data[1::2]
    left_list.sort()
    right_list.sort()
    return left_list, right_list


def difference(data: list[int]) -> list[int]:
    left_list, right_list = separate_list(data)
    diff = [abs(left - right) for left, right in zip(left_list, right_list)]
    return diff


def similarity_score(left_list: list[int], right_list: list[int]) -> int:
    right_counter = Counter(right_list)
    score = sum(left * right_counter[left] for left in left_list)
    return score


def part_one(data: list[int]) -> int:
    diff = difference(data)
    result = sum(diff)
    print(result)
    return result


part_one(data)
aoc_helper.lazy_test(day=1, year=2024, parse=parse_raw, solution=part_one)


def part_two(data=list[int]) -> int:
    left_list, right_list = separate_list(data)
    score = similarity_score(left_list, right_list)
    print(score)
    return score


part_two(data)
aoc_helper.lazy_test(day=1, year=2024, parse=parse_raw, solution=part_two)

aoc_helper.lazy_submit(day=1, year=2024, solution=part_one, data=data)
aoc_helper.lazy_submit(day=1, year=2024, solution=part_two, data=data)
