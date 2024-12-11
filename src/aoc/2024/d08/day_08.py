from collections import Counter, defaultdict, deque
import numpy as np
import string
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

raw = aoc_helper.fetch(8, 2024)


def parse_raw(input: str) -> np.ndarray:
    lines = input.split("\n")
    print(f"Number of lines: {len(lines)}")  # Debugging statement
    for i, line in enumerate(lines):  # Print the first 5 lines for verification
        print(f"Line {i + 1}: {line}")
    return [list(line) for line in lines]


data = parse_raw(raw)


# Print the length of the y and x axes
y_length = len(data)
x_length = len(data[0]) if y_length > 0 else 0

print(f"Length of y-axis: {y_length}")
print(f"Length of x-axis: {x_length}")
# Updated test input
# data = np.array(
#     [
#         [".", ".", ".", ".", ".", "#", ".", ".", ".", ".", "#"],
#         [".", ".", ".", "#", ".", ".", ".", ".", "0", ".", "."],
#         [".", ".", ".", ".", "#", "0", ".", ".", ".", "#", "."],
#         [".", ".", "#", ".", ".", ".", ".", "0", ".", ".", "."],
#         [".", ".", ".", ".", "0", ".", ".", ".", "#", ".", "."],
#         [".", "#", ".", ".", ".", ".", "A", ".", ".", ".", "."],
#         [".", ".", ".", "#", ".", ".", ".", ".", ".", ".", "."],
#         ["#", ".", ".", ".", ".", ".", "#", ".", ".", ".", "."],
#         [".", ".", ".", ".", ".", ".", ".", "A", ".", ".", "."],
#         [".", ".", ".", ".", ".", ".", ".", ".", "A", ".", "."],
#         [".", ".", ".", ".", ".", ".", ".", ".", ".", "#", "."],
#         [".", ".", ".", ".", ".", ".", ".", ".", ".", "#", "."],
#     ]
# )


def find_all_occurrences(grid: np.ndarray, char: str) -> list:
    occurrences = []
    for y in range(len(grid)):
        for x in range(len(grid[0])):
            if grid[y][x] == char:
                occurrences.append((y, x))
    return occurrences


def calculate_vectors(grid: np.ndarray, char: str) -> set:
    antinodes = set()
    occurrences = find_all_occurrences(grid, char)

    for start_pos in occurrences:
        y, x = start_pos
        for occurrence in occurrences:
            if occurrence == start_pos:
                continue  # Skip the starting position
            vector_y = occurrence[0] - y
            vector_x = occurrence[1] - x
            antinode_y = y + 2 * vector_y
            antinode_x = x + 2 * vector_x
            if 0 <= antinode_y < len(grid) and 0 <= antinode_x < len(grid[0]):
                antinodes.add((antinode_y, antinode_x))

    return antinodes


def update_grid(grid: np.ndarray, antinodes: set, char: str) -> np.ndarray:
    new_grid = grid.copy()
    for y, x in antinodes:
        new_grid[y][x] = char
    return new_grid


def part_one(data=data):
    # Example usage
    characters = string.ascii_letters + string.digits
    unique_antinodes = set()

    for char in characters:
        antinodes = calculate_vectors(data, char)
        unique_antinodes.update(antinodes)
        print(f"Character: {char}, Antinodes: {antinodes}")

    print("Unique Antinodes:", unique_antinodes)
    return len(unique_antinodes)


def part_two(data=data):
    characters = string.ascii_letters + string.digits
    unique_antinodes = set()

    for char in characters:
        grid = data.copy()
        while True:
            antinodes = calculate_vectors(grid, char)
            if not antinodes - unique_antinodes:
                break
            unique_antinodes.update(antinodes)
            grid = update_grid(grid, antinodes, char)
            # print(f"Character: {char}, Extended Antinodes: {antinodes}")

    print("Unique Antinodes:", unique_antinodes)
    return len(unique_antinodes)


# Run the test
# print("Total Unique Antinodes:", part_one(data))


# aoc_helper.lazy_test(day=8, year=2024, parse=parse_raw, solution=part_one)


# Run the test for part two
print("Total Unique Antinodes (Part Two):", part_two(data))

aoc_helper.lazy_test(day=8, year=2024, parse=parse_raw, solution=part_two)

# aoc_helper.lazy_submit(day=8, year=2024, solution=part_one, data=data)
# aoc_helper.lazy_submit(day=8, year=2024, solution=part_two, data=data)
