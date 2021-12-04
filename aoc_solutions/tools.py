from aocd.models import Puzzle
import numpy as np
import pandas as pd
from pathlib import Path


PROJECT_DIR = Path(__file__).resolve().parents[1]


class NumPuzzle(Puzzle):
    def __init__(self, day, *args, **kwargs):
        super().__init__(day=day, *args, **kwargs)
        with open(PROJECT_DIR / f"example_data/day_{self.day}/input") as f:
            self.example_data = f.read().strip()
        with open(PROJECT_DIR / f"example_data/day_{self.day}/answer_one") as f:
            self.example_answer_one = f.read().strip()
        with open(PROJECT_DIR / f"example_data/day_{self.day}/answer_two") as f:
            self.example_answer_two = f.read().strip()

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
