from typing import List, Tuple
import aoc_helper
from aoc_helper import (
    list,
    map,
    range,
)
from typing import List, Tuple


raw = aoc_helper.fetch(5, 2024)


def parse_raw(raw: str):
    return raw.split("\n\n")


data = parse_raw(raw)


def page_ordering_rules(data: str) -> List[Tuple[int, int]]:
    return [tuple(map(int, line.split("|"))) for line in data.split("\n")]


def page_numbers_of_each_update(data: str) -> List[List[int]]:
    return [list(map(int, line.split(","))) for line in data.strip().split("\n")]


def is_valid_update(update: List[int], rules: List[Tuple[int, int]]) -> bool:
    return all(
        (update[i], update[j]) in rules
        for i in range(len(update))
        for j in range(i + 1, len(update))
    )


def find_middle_numbers(
    updates: List[List[int]], rules: List[Tuple[int, int]], valid_only: bool = True
) -> List[int]:
    middle_numbers = []
    for update in updates:
        if valid_only and is_valid_update(update, rules):
            middle_index = len(update) // 2
            middle_numbers.append(update[middle_index])
        elif not valid_only and not is_valid_update(update, rules):
            sorted_update = sort_update(update, rules)
            middle_index = len(sorted_update) // 2
            middle_numbers.append(sorted_update[middle_index])
    return middle_numbers


# topological sort based on somw provided custom rules.
def sort_update(update: List[int], rules: List[Tuple[int, int]]) -> List[int]:
    sorted_update = []
    remaining = set(update)
    while remaining:
        for num in list(remaining):
            if all((num, other) in rules for other in remaining if other != num):
                sorted_update.append(num)
                remaining.remove(num)
                break
    return sorted_update


def part_one(data=data):
    rules = page_ordering_rules(data[0])
    updates = page_numbers_of_each_update(data[1])
    middle_numbers = find_middle_numbers(updates, rules, valid_only=True)
    print(sum(middle_numbers))
    return sum(middle_numbers)


def part_two(data=data):
    rules = page_ordering_rules(data[0])
    updates = page_numbers_of_each_update(data[1])
    middle_numbers = find_middle_numbers(updates, rules, valid_only=False)
    print(sum(middle_numbers))
    return sum(middle_numbers)


aoc_helper.lazy_test(day=5, year=2024, parse=parse_raw, solution=part_one)
aoc_helper.lazy_test(day=5, year=2024, parse=parse_raw, solution=part_two)

aoc_helper.lazy_submit(day=5, year=2024, solution=part_one, data=data)
aoc_helper.lazy_submit(day=5, year=2024, solution=part_two, data=data)
