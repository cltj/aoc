
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

raw = aoc_helper.fetch(10, 2022)


def parse_raw(raw: str):
    return ...


data = parse_raw(raw)


# providing this default is somewhat of a hack - there isn't any other way to
# force type inference to happen, AFAIK - but this won't work with standard
# collections (list, set, dict, tuple)
def part_one(data=data):
    ...


aoc_helper.lazy_test(day=10, year=2022, parse=parse_raw, solution=part_one)


# providing this default is somewhat of a hack - there isn't any other way to
# force type inference to happen, AFAIK - but this won't work with standard
# collections (list, set, dict, tuple)
def part_two(data=data):
    ...


aoc_helper.lazy_test(day=10, year=2022, parse=parse_raw, solution=part_two)

aoc_helper.lazy_submit(day=10, year=2022, solution=part_one, data=data)
aoc_helper.lazy_submit(day=10, year=2022, solution=part_two, data=data)