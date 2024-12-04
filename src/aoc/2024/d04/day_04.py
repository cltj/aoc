from collections import Counter, defaultdict, deque
import numpy as np
from collections import namedtuple
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

raw = aoc_helper.fetch(4, 2024)


def parse_raw(raw: str):
    lines = raw.split("\n")
    grid = [list(line) for line in lines]

    # Print column indices
    col_indices = "   " + " ".join(f"{i:2}" for i in range(len(grid[0])))
    print(col_indices)

    # Print each row with its index
    for idx, row in enumerate(grid):
        row_str = " ".join(row)
        print(f"{idx:2} {row_str}")

    return grid


data = parse_raw(raw)
Direction = namedtuple("Direction", ["dx", "dy", "name"])


def find_word(grid, word):
    directions = [
        Direction(0, 1, "right"),
        Direction(0, -1, "left"),
        Direction(1, 0, "down"),
        Direction(-1, 0, "up"),
        Direction(1, 1, "down-right"),
        Direction(-1, -1, "up-left"),
        Direction(1, -1, "down-left"),
        Direction(-1, 1, "up-right"),
    ]
    word_length = len(word)
    rows, cols = len(grid), len(grid[0])
    found_positions = []

    def is_valid(x, y):
        return 0 <= x < rows and 0 <= y < cols

    def search_from(x, y, dx, dy):
        for i in range(word_length):
            nx, ny = x + i * dx, y + i * dy
            if not is_valid(nx, ny) or grid[nx][ny] != word[i]:
                return False
        return True

    for x in range(rows):
        for y in range(cols):
            if grid[x][y] == word[0]:
                for dx, dy, name in directions:
                    if search_from(x, y, dx, dy):
                        found_positions.append((x, y, dx, dy, name))

    return found_positions


def replace_x_with_dot(grid):
    for x in range(len(grid)):
        for y in range(len(grid[0])):
            if grid[x][y] == "X":
                grid[x][y] = "."
    return grid


def find_mas_x(grid):
    patterns = [
        [(0, 0), (1, 1), (2, 2)],  # Down-right diagonal
        [(0, 2), (1, 1), (2, 0)],  # Down-left diagonal
        [(2, 0), (1, 1), (0, 2)],  # Up-right diagonal
        [(2, 2), (1, 1), (0, 0)],  # Up-left diagonal
    ]
    rows, cols = len(grid), len(grid[0])
    found_positions = []

    def is_valid(x, y):
        return 0 <= x < rows and 0 <= y < cols

    def search_pattern(x, y, pattern):
        for dx, dy in pattern:
            nx, ny = x + dx, y + dy
            if not is_valid(nx, ny):
                return False
            if (
                (dx, dy) == (0, 0)
                or (dx, dy) == (2, 2)
                or (dx, dy) == (0, 2)
                or (dx, dy) == (2, 0)
            ):
                if grid[nx][ny] != "M":
                    return False
            elif (dx, dy) == (1, 1):
                if grid[nx][ny] != "A":
                    return False
            elif (
                (dx, dy) == (2, 2)
                or (dx, dy) == (0, 0)
                or (dx, dy) == (2, 0)
                or (dx, dy) == (0, 2)
            ):
                if grid[nx][ny] != "S":
                    return False
        return True

    for x in range(rows):
        for y in range(cols):
            for pattern in patterns:
                if search_pattern(x, y, pattern):
                    found_positions.append((x, y, pattern))

    return found_positions


def part_one(data=data):
    word = "XMAS"
    return len(find_word(data, word))


aoc_helper.lazy_test(day=4, year=2024, parse=parse_raw, solution=part_one)


def part_two(data=data):
    grid = replace_x_with_dot(data)
    found_positions = find_mas_x(grid)
    return len(found_positions)


# aoc_helper.lazy_test(day=4, year=2024, parse=parse_raw, solution=part_two)

aoc_helper.lazy_submit(day=4, year=2024, solution=part_one, data=data)
# aoc_helper.lazy_submit(day=4, year=2024, solution=part_two, data=data)
