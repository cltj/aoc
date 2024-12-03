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

raw = aoc_helper.fetch(2, 2024)


def parse_raw(raw: str):
    groups = raw.strip().split("\n")
    parsed_groups = [list(map(int, group.split())) for group in groups]
    return parsed_groups


data = parse_raw(raw)


def all_desc_or_asc(lst):
    increasing = True
    decreasing = True
    for i in range(1, len(lst)):
        if lst[i] < lst[i - 1]:
            increasing = False
        if lst[i] > lst[i - 1]:
            decreasing = False
    return increasing or decreasing


def pair_is_valid(lst):
    for i in range(1, len(lst)):
        diff = abs(lst[i] - lst[i - 1])
        if diff < 1 or diff > 3:
            return False
    return True


def valid_check(lst):
    if all_desc_or_asc(lst) and pair_is_valid(lst):
        return True
    return False


def problem_dampner(data):
    valid_counter = 0
    for lst in data:
        if valid_check(lst):
            valid_counter += 1
        else:
            original_lst = lst[:]
            for i in range(len(original_lst)):
                new_lst = original_lst[:i] + original_lst[i + 1 :]
                if valid_check(new_lst):
                    valid_counter += 1
                    break
    return valid_counter


def part_one(data=data):
    valid = 0
    for lst in data:
        if valid_check(lst):
            valid += 1
    print(valid)
    return valid


def part_two(data=data):
    valid = problem_dampner(data)
    print(valid)
    return valid


aoc_helper.lazy_test(day=2, year=2024, parse=parse_raw, solution=part_one)
aoc_helper.lazy_test(day=2, year=2024, parse=parse_raw, solution=part_two)

aoc_helper.lazy_submit(day=2, year=2024, solution=part_one, data=data)
aoc_helper.lazy_submit(day=2, year=2024, solution=part_two, data=data)
