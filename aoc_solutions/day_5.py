from copy import deepcopy

import numpy as np

from aoc_solutions.tools import PuzzleExt, test_and_submit
import re
from functools import reduce, partial
from itertools import repeat


def split(line): return re.split(",| -> ", line)


def intify(it):
    return tuple(map(int, it))


def inclusive_range(start, stop): return range(start, stop + 1) if stop >= start else range(start, stop - 1, -1)


def ventcoords(vl, incdiag):
    if vl[1] == vl[3]:
        return zip(inclusive_range(vl[0], vl[2]), repeat(vl[1], abs(vl[2] - vl[0]) + 1))
    if vl[0] == vl[2]:
        return zip(repeat(vl[0], abs(vl[3] - vl[1]) + 1), inclusive_range(vl[1], vl[3]))
    return zip(inclusive_range(vl[0], vl[2]), inclusive_range(vl[1], vl[3])) if incdiag else tuple()


ventcoords_hor_ver = partial(ventcoords, incdiag=False)
ventcoords_diag = partial(ventcoords, incdiag=True)


def pad_if_needed(diag, desired_x, desired_y):
    x, y = diag.shape
    if x >= desired_x and y >= desired_y:
        return diag
    new = np.zeros((max(desired_x, x), max(desired_y, y)), dtype=int)
    new[:diag.shape[0], :diag.shape[1]] = diag
    return new


def update(diagram, ventcoords):
    cp = deepcopy(diagram)
    for x, y in ventcoords:
        cp = pad_if_needed(cp, x+1, y+1)
        cp[x, y] += 1
    return cp


def count(diagram):
    return (diagram > 1).sum()


def solve_part_one(lines) -> int:
    lines_split = map(split, lines)
    lines_int = map(intify, lines_split)
    coords = map(ventcoords_hor_ver, lines_int)
    nonempty_coords = filter(lambda x: x != tuple(), coords)
    diag = reduce(update, nonempty_coords, np.zeros((1, 1)))
    return count(diag)


def solve_part_two(lines) -> int:
    lines_split = map(split, lines)
    lines_int = map(intify, lines_split)
    coords = map(ventcoords_diag, lines_int)
    nonempty_coords = filter(lambda x: x != tuple(), coords)
    diag = reduce(update, nonempty_coords, np.zeros((1, 1)))
    return count(diag)


if __name__ == '__main__':
    puzzle = PuzzleExt()
    example_data = puzzle.example_data_str_series
    real_data = puzzle.input_data_str_series
    test_and_submit(puzzle, solve_part_one, solve_part_two, example_data, real_data)
