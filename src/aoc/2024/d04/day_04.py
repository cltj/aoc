import numpy as np
import aoc_helper
from aoc_helper import list, map


raw = aoc_helper.fetch(4, 2024)

ALL_DIRECTIONS = [(0, 1), (1, 1), (1, 0), (-1, 1), (-1, 0), (-1, -1), (0, -1), (1, -1)]
DIAGONALS = [[(-1, -1), (0, 0), (1, 1)], [(-1, 1), (0, 0), (1, -1)]]


def parse_raw(input: str) -> np.ndarray:
    return np.array([list(line) for line in input.splitlines()])


def letter_positions(grid: np.ndarray, letter: str) -> list[tuple[int, int]]:
    return list((int(x), int(y)) for x, y in zip(*np.where(grid == letter)))


def is_in_grid(grid: np.ndarray, coordinates: tuple[int, int]) -> bool:
    return all(0 <= coordinates[axis] < grid.shape[axis] for axis in (0, 1))


def count_xmas_spelled(grid: np.ndarray, coordinates: tuple[int, int]) -> int:
    return sum(
        spells_xmas(grid, coordinates, direction) for direction in ALL_DIRECTIONS
    )


def spells_xmas(
    grid: np.ndarray, coordinates: tuple[int, int], direction: tuple[int, int]
) -> bool:
    target = "XMAS"
    for target_char in target:
        if not (is_in_grid(grid, coordinates) and grid[coordinates] == target_char):
            return False
        coordinates = tuple(map(sum, zip(direction, coordinates)))
    return True


def is_x_shaped_mas(grid: np.ndarray, coordinates: tuple[int, int]) -> bool:
    target = "MAS"
    for diagonal in DIAGONALS:
        all_coordinates = [
            (coordinates[0] + d[0], coordinates[1] + d[1]) for d in diagonal
        ]
        if not all(is_in_grid(grid, c) for c in all_coordinates):
            return False
        if "".join(grid[c] for c in all_coordinates) not in [target, target[::-1]]:
            return False
    return True


def part_one(grid: np.ndarray) -> int:
    return sum(count_xmas_spelled(grid, x) for x in letter_positions(grid, "X"))


def part_two(grid: np.ndarray) -> int:
    return sum(1 for a in letter_positions(grid, "A") if is_x_shaped_mas(grid, a))


data = parse_raw(raw)

aoc_helper.lazy_test(day=4, year=2024, parse=parse_raw, solution=part_one)
aoc_helper.lazy_test(day=4, year=2024, parse=parse_raw, solution=part_two)

aoc_helper.lazy_submit(day=4, year=2024, solution=part_one, data=data)
aoc_helper.lazy_submit(day=4, year=2024, solution=part_two, data=data)
