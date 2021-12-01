from aocd.models import Puzzle
import numpy as np


class NumPuzzle(Puzzle):
    @property
    def input_data_num(self):
        return [int(n) for n in self.input_data.splitlines()]

    @property
    def input_data_array(self):
        return np.array(self.input_data_num)
