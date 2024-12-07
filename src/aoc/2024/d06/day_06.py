from collections import Counter, defaultdict, deque
import numpy as np
from colorama import Fore, Style, init
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

init(autoreset=True)


DIRECTIONS = [(0, 1), (1, 0), (0, -1), (-1, 0)]  # Right, Down, Left, Up
DIRECTION_WORDS = {(0, 1): "RIGHT", (1, 0): "DOWN", (0, -1): "LEFT", (-1, 0): "UP"}


def parse_raw(input: str) -> np.ndarray:
    return np.array([list(line) for line in input.splitlines()])


def add_grid_edges(grid: np.ndarray) -> np.ndarray:
    vertical = len(grid) + 2
    horizontal = len(grid[0]) + 2

    # Create a new grid with the required dimensions
    new_grid = np.full((vertical, horizontal), "/")

    # Copy the original grid into the new grid, leaving a border of '/'
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            new_grid[i + 1][j + 1] = grid[i][j]

    return new_grid


def find_start(grid):
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == "^":
                return i, j


def get_next_direction(current_direction: tuple[int, int]) -> tuple[int, int]:
    current_index = DIRECTIONS.index(current_direction)
    next_index = (current_index + 1) % len(DIRECTIONS)
    return DIRECTIONS[next_index]


def walk(grid: np.ndarray, start: tuple[int, int], max_steps: int = None) -> np.ndarray:
    i, j = start
    direction = (-1, 0)  # Start by moving up
    steps = 0
    while max_steps is None or steps < max_steps:
        next_i, next_j = i + direction[0], j + direction[1]
        print(
            f"Current position: ({i}, {j}), direction: {DIRECTION_WORDS[direction]}, next position: ({next_i}, {next_j})"
        )
        if grid[next_i][next_j] == "#":
            direction = get_next_direction(direction)
            print(
                f"Encountered {Fore.YELLOW}#{Style.RESET_ALL}, changing direction to: {DIRECTION_WORDS[direction]}"
            )
        else:
            grid[i][j] = "X"
            i, j = next_i, next_j
            steps += 1
        if grid[i][j] == "/":  # Stop if we reach the edge
            break
    grid[i][j] = "@"  # Mark the current position with '@'
    return grid, (i, j)


def print_grid(grid: np.ndarray, current_position: tuple[int, int]):
    for i, row in enumerate(grid):
        for j, cell in enumerate(row):
            if (i, j) == current_position:
                print(Fore.BLUE + cell, end="")
            elif cell == "X":
                print(Fore.GREEN + cell, end="")
            elif cell == "#":
                print(Fore.RED + cell, end="")
            else:
                print(cell, end="")
        print()


def count_steps(grid: np.ndarray) -> int:
    return Counter(grid.flatten())["X"]


# Example data
# raw_example = """
# ....#.....
# .........#
# ..........
# ..#.......
# .......#..
# ..........
# .#..^.....
# ........#.
# #.........
# ......#..."""

raw = aoc_helper.fetch(6, 2024)
data = parse_raw(raw)
boxed_grid = add_grid_edges(data)
walked_grid, current_position = walk(boxed_grid, find_start(boxed_grid), max_steps=None)
print_grid(walked_grid, current_position)
print(count_steps(walked_grid))


# def part_one(data=data):
#     boxed_grid = add_grid_edges(data)
#     walked_grid, current_position = walk(
#         boxed_grid, find_start(boxed_grid), max_steps=None
#     )
#     return count_steps(walked_grid)


# aoc_helper.lazy_test(day=6, year=2024, parse=parse_raw, solution=part_one)


# def part_two(data=data): ...


# aoc_helper.lazy_test(day=6, year=2024, parse=parse_raw, solution=part_two)

# aoc_helper.lazy_submit(day=6, year=2024, solution=part_one, data=data)
# aoc_helper.lazy_submit(day=6, year=2024, solution=part_two, data=data)
