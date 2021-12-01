from aoc_solutions.tools import NumPuzzle
import numpy as np


def solve_part_a(numbers: np.ndarray) -> int:
    return(numbers[1:] > numbers[:-1]).sum()


def solve_part_b(numbers: np.ndarray) -> int:
    sum_of_three = np.convolve(numbers, np.ones(3), 'valid')
    return solve_part_a(sum_of_three)


if __name__ == '__main__':
    puzzle = NumPuzzle(day=1, year=2021)
    test_data = np.array([199, 200, 208, 210, 200, 207, 240, 269, 260, 263])
    real_data = puzzle.input_data_array

    if solve_part_a(test_data) == 7:
        puzzle.answer_a = solve_part_a(real_data)

    if solve_part_b(test_data) == 5:
        puzzle.answer_b = solve_part_b(real_data)
