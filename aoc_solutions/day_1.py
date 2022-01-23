from aoc_solutions.tools import PuzzleExt
import numpy as np


def solve_part_one(numbers: np.ndarray) -> int:
    return (numbers[1:] > numbers[:-1]).sum()


def solve_part_two(numbers: np.ndarray) -> int:
    sum_of_three = np.convolve(numbers, np.ones(3), 'valid')
    return solve_part_one(sum_of_three)


if __name__ == '__main__':
    puzzle = PuzzleExt(day=1, year=2021)
    print(puzzle.input_data)
    example_data = puzzle.example_data_array
    real_data = puzzle.input_data_array

    if (result := solve_part_one(example_data)) == puzzle.example_answer_one:
        print(f'Part one: {result} is the correct answer with example data')
        puzzle.answer_a = solve_part_one(real_data)
    else:
        print(f'Part one: {result} is wrong, should be {puzzle.example_answer_one}')

    if (result := solve_part_two(example_data)) == puzzle.example_answer_two:
        print(f'Part two: {result} is the correct answer with example data')
        puzzle.answer_b = solve_part_two(real_data)
    else:
        print(f'Part two: {result} is wrong, should be {puzzle.example_answer_two}')