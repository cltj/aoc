from aoc_solutions.tools import NumPuzzle
import numpy as np


def solve_part_one(numbers: np.ndarray) -> int:
    return (numbers[1:] > numbers[:-1]).sum()


def solve_part_two(numbers: np.ndarray) -> int:
    sum_of_three = np.convolve(numbers, np.ones(3), 'valid')
    return solve_part_one(sum_of_three)


if __name__ == '__main__':
    puzzle = NumPuzzle(day=1, year=2021)
    example_data = puzzle.example_data_array
    real_data = puzzle.input_data_array

    if solve_part_one(example_data) == puzzle.example_answer_one:
        puzzle.answer_a = solve_part_one(real_data)

    if solve_part_two(example_data) == puzzle.example_answer_two:
        puzzle.answer_b = solve_part_two(real_data)
