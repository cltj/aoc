from collections import Counter, defaultdict, deque
import numpy as np
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

raw = aoc_helper.fetch(1, 2022)


def parse_raw(raw: str):
    return raw


data = parse_raw(raw)


# providing this default is somewhat of a hack - there isn't any other way to
# force type inference to happen, AFAIK - but this won't work with standard
# collections (list, set, dict, tuple)
def part_one(data) -> int:
    groups = data.strip().split("\n\n")
    max_sum = 0

    for group in groups:
        numbers = np.array(group.split(), dtype=int)
        group_sum = np.sum(numbers)
        if group_sum > max_sum:
            max_sum = group_sum

    return max_sum


aoc_helper.lazy_test(day=1, year=2022, parse=parse_raw, solution=part_one)


# providing this default is somewhat of a hack - there isn't any other way to
# force type inference to happen, AFAIK - but this won't work with standard
# collections (list, set, dict, tuple)
def part_two(data=data):
    groups = data.strip().split("\n\n")
    sums = []

    for group in groups:
        numbers = np.array(group.split(), dtype=int)
        group_sum = np.sum(numbers)
        sums.append(group_sum)

    top_three_sums = sorted(sums, reverse=True)[:3]
    total_top_three = np.sum(top_three_sums)

    return total_top_three


aoc_helper.lazy_test(day=1, year=2022, parse=parse_raw, solution=part_two)

aoc_helper.lazy_submit(day=1, year=2022, solution=part_one, data=data)
aoc_helper.lazy_submit(day=1, year=2022, solution=part_two, data=data)
