import aoc_helper
from aoc_helper import list, map, range

raw = aoc_helper.fetch(2, 2024)


def parse_raw(raw: str):
    groups = raw.strip().split("\n")
    return [list(map(int, group.split())) for group in groups]


data = parse_raw(raw)


def all_desc_or_asc(lst):
    return all(lst[i] >= lst[i - 1] for i in range(1, len(lst))) or all(
        lst[i] <= lst[i - 1] for i in range(1, len(lst))
    )


def pair_is_valid(lst):
    return all(1 <= abs(lst[i] - lst[i - 1]) <= 3 for i in range(1, len(lst)))


def valid_check(lst):
    return all_desc_or_asc(lst) and pair_is_valid(lst)


def problem_dampner(data):
    valid_counter = 0
    for lst in data:
        if valid_check(lst):
            valid_counter += 1
        else:
            for i in range(len(lst)):
                new_lst = lst[:i] + lst[i + 1 :]
                if valid_check(new_lst):
                    valid_counter += 1
                    break
    return valid_counter


def part_one(data=data):
    return sum(1 for lst in data if valid_check(lst))


def part_two(data=data):
    return problem_dampner(data)


aoc_helper.lazy_test(day=2, year=2024, parse=parse_raw, solution=part_one)
aoc_helper.lazy_test(day=2, year=2024, parse=parse_raw, solution=part_two)

aoc_helper.lazy_submit(day=2, year=2024, solution=part_one, data=data)
aoc_helper.lazy_submit(day=2, year=2024, solution=part_two, data=data)
