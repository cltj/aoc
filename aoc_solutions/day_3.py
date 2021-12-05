import numpy as np
from itertools import cycle
from aoc_solutions.tools import PuzzleExt


def solve_part_one(lines: list) -> int:
    data = np.array([list(line) for line in lines], dtype=int).astype(bool)
    bin_count = np.apply_along_axis(np.bincount, axis=0, arr=data)
    gamma_rate = int("".join(list(np.argmax(bin_count, 0).astype(str))), 2)
    epsilon_rate = int("".join(list(np.argmax(np.invert(bin_count), 0).astype(str))), 2)
    return gamma_rate * epsilon_rate


def lines_with_most_common_char(lines: list, pos: int) -> list:
    counts = [0, 0]
    for line in lines:
        counts[int(line[pos])] += 1
    if counts[0] == counts[1]:
        most_common = 1
    else:
        most_common = counts.index(max(counts))
    return [line for line in lines if int(line[pos]) == most_common]


def lines_with_least_common_char(lines: list, pos: int) -> list:
    counts = [0, 0]
    for line in lines:
        counts[int(line[pos])] += 1
    if counts[0] == counts[1]:
        least_common = 0
    else:
        least_common = counts.index(min(counts))
    return [line for line in lines if int(line[pos]) == least_common]


def solve_part_two(lines: list) -> int:
    ratings = []
    for lst, filter_func in [[lines, lines_with_most_common_char], [lines.copy(), lines_with_least_common_char]]:
        for pos in cycle(range(12)):
            lst = filter_func(lst, pos)
            if len(lst) == 1:
                break
        ratings.append(int(lst[0], 2))
    return ratings[0] * ratings[1]


if __name__ == '__main__':
    puzzle = PuzzleExt()
    example_data = puzzle.example_data_list
    real_data = puzzle.input_data_list

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
