import inspect

from aocd.models import Puzzle
import numpy as np
import pandas as pd
from pathlib import Path
import re


PROJECT_DIR = Path(__file__).resolve().parents[1]


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
