import inspect

from aocd.models import Puzzle
import numpy as np
import pandas as pd
from pathlib import Path
import re


PROJECT_DIR = Path(__file__).resolve().parents[1]


def test_and_submit(puzzle, solve_part_one, solve_part_two, example_data, real_data):
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


class PuzzleExt(Puzzle):
    def __init__(self, day=None, year=2021, *args, **kwargs):
        if day is None:
            caller_filename = inspect.getmodule(inspect.stack()[1][0]).__file__
            day = int(re.search(r'\d+', caller_filename).group())
        super().__init__(day=day, year=year, *args, **kwargs)
        with open(PROJECT_DIR / f"example_data/day_{self.day}/input") as f:
            self.example_data = f.read().strip()
        with open(PROJECT_DIR / f"example_data/day_{self.day}/answer_one") as f:
            answer_one = f.read().strip()
            try:
                self.example_answer_one = int(answer_one)
            except ValueError:
                self.example_answer_one = answer_one
        with open(PROJECT_DIR / f"example_data/day_{self.day}/answer_two") as f:
            answer_two = f.read().strip()
            try:
                self.example_answer_two = int(answer_two)
            except ValueError:
                self.example_answer_two = answer_two

    @property
    def input_data_list(self):
        return self.input_data.splitlines()

    @property
    def input_data_num(self):
        return [int(n) for n in self.input_data_list]

    @property
    def input_data_array(self):
        return np.array(self.input_data_num)

    @property
    def input_data_series(self):
        return pd.Series(self.input_data_num)

    @property
    def input_data_str_series(self):
        return pd.Series(self.input_data_list)

    @property
    def example_data_list(self):
        return self.example_data.splitlines()

    @property
    def example_data_num(self):
        return [int(n) for n in self.example_data_list]

    @property
    def example_data_array(self):
        return np.array(self.example_data_num)

    @property
    def example_data_series(self):
        return pd.Series(self.example_data_num)

    @property
    def example_data_str_series(self):
        return pd.Series(self.example_data_list)
