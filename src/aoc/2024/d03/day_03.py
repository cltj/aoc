import re
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

raw = aoc_helper.fetch(3, 2024)


def parse_raw(raw: str):
    return raw


data = parse_raw(raw)


def extract_mul_expressions(text):
    # Define the regex pattern to match mul(x,y)
    pattern = r"mul\(\d+,\d+\)"
    # Find all matches in the text
    matches = re.findall(pattern, text)
    return matches


def group_text(text):
    results = []
    parts = data.split("do")
    pre_do_part = parts[0]
    mul_expressions = extract_mul_expressions(pre_do_part)
    for expr in mul_expressions:
        x, y = map(int, extract_ints(expr))
        results.append(x * y)

    # Process the parts after each "do"
    for part in parts[1:]:
        if part.startswith("n't"):
            continue
        mul_expressions = extract_mul_expressions(part)
        for expr in mul_expressions:
            x, y = map(int, extract_ints(expr))
            results.append(x * y)
    total_sum = sum(results)
    print(total_sum)
    return total_sum


def part_one(data=data):
    mul_expressions = extract_mul_expressions(data)
    results = []
    for expr in mul_expressions:
        # Extract the two numbers from the expression
        x, y = map(int, extract_ints(expr))
        # Multiply the two numbers
        result = x * y
        results.append(result)
        # Replace the expression with the result
        data = data.replace(expr, str(result))
    print(sum(results))
    return sum(results)


def part_two(data=data):
    results = []
    parts = data.split("do")
    pre_do_part = parts[0]
    mul_expressions = extract_mul_expressions(pre_do_part)
    for expr in mul_expressions:
        x, y = map(int, extract_ints(expr))
        results.append(x * y)

    # Process the parts after each "do"
    for part in parts[1:]:
        if part.startswith("n't"):
            continue
        mul_expressions = extract_mul_expressions(part)
        for expr in mul_expressions:
            x, y = map(int, extract_ints(expr))
            results.append(x * y)
    total_sum = sum(results)
    print(total_sum)
    return total_sum


aoc_helper.lazy_test(day=3, year=2024, parse=parse_raw, solution=part_one)
aoc_helper.lazy_test(day=3, year=2024, parse=parse_raw, solution=part_two)

aoc_helper.lazy_submit(day=3, year=2024, solution=part_one, data=data)
aoc_helper.lazy_submit(day=3, year=2024, solution=part_two, data=data)
