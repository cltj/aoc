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


def all_increasing(lst):
    for i in range(1, len(lst)):
        if lst[i] <= lst[i - 1]:
            return False
    return True


def all_decreasing(lst):
    for i in range(1, len(lst)):
        if lst[i] >= lst[i - 1]:
            return False
    return True


def adjacent_numbers_more_than_three_apart(lst):
    for i in range(1, len(lst)):
        if abs(lst[i] - lst[i - 1]) > 3:
            return True
    return False


def equal_pairs(lst):
    for i in range(1, len(lst)):
        if lst[i] == lst[i - 1]:
            return True
    return False


def remove_on_equal_pairs(lst):
    i = 1
    while i < len(lst):
        if lst[i] == lst[i - 1]:
            lst.pop(i)
        else:
            i += 1
    return lst


def product_dampener(lst):
    lst = remove_on_equal_pairs(lst)
    parts = []
    if all_increasing(lst) or all_decreasing(lst):
        parts.append(True)
    if not adjacent_numbers_more_than_three_apart(lst):
        parts.append(True)

    if parts.count(True) >= 1:
        return True
    else:
        return False


# lst = [1, 2, 2, 3, 4, 4, 5, 6, 7, 8, 9, 9, 10]
# lst1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 8]
# lst3 = [1, 2, 3, 4, 5, 9, 10]
# lst4 = [1, 2, 7, 8, 9, 8]
# print(product_dampener(lst))  # True
# print(product_dampener(lst1))  # True
# print(product_dampener(lst3))  # True
# print(product_dampener(lst4))  # False


def valid_raport(lst):
    if product_dampener(lst):
        return 1
    elif all_increasing(lst) or all_decreasing(lst):
        if not adjacent_numbers_more_than_three_apart(lst):
            return 1
    else:
        return 0


def part_one(data=data):
    valid = 0
    for group in data:
        valid += valid_raport(group)
    print(valid)
    return valid


# part_one(data)
# # aoc_helper.lazy_test(day=2, year=2024, parse=parse_raw, solution=part_one)


def part_two(data=data):
    valid = 0
    for group in data:
        valid += valid_raport(group)
    print(valid)
    return valid


# part_one(data)
part_two(data)
aoc_helper.lazy_test(day=2, year=2024, parse=parse_raw, solution=part_two)

# aoc_helper.lazy_submit(day=2, year=2024, solution=part_one, data=data)
# aoc_helper.lazy_submit(day=2, year=2024, solution=part_two, data=data)
