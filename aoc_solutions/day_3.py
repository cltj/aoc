from aoc_solutions.tools import PuzzleExt


def solve_part_one(lines: list) -> int:
    ...


def solve_part_two(lines: list) -> int:
    ...


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
