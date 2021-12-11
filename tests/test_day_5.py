import numpy as np

from aoc_solutions.day_5 import split, inclusive_range, ventcoords, update, count, pad_if_needed


def test_split():
    assert split("1,2 -> 3,4") == ["1", "2", "3", "4"]


def test_inclusive_range():
    assert list(inclusive_range(3, 7)) == [3, 4, 5, 6, 7]
    assert list(inclusive_range(3, 3)) == [3]
    assert list(inclusive_range(7, 3)) == [7, 6, 5, 4, 3]


def test_ventcoords():
    assert tuple(ventcoords([1, 3, 1, 7])) == ((1, 3), (1, 4), (1, 5), (1, 6), (1, 7))
    assert tuple(ventcoords([1, 7, 1, 3])) == ((1, 7), (1, 6), (1, 5), (1, 4), (1, 3))


def test_update():
    diagram = [[0] * 10 for _ in range(10)]
    ventcorrds = ((1, 3), (1, 4), (1, 5), (1, 6), (1, 7))
    assert update(diagram, ventcorrds) == [
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 1, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 1, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 1, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 1, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 1, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    ]


def test_pad_if_needed():
    diag = np.array([
        [1, 2, 3],
        [4, 5, 6],
    ])
    expected = np.array([
        [1, 2, 3, 0, 0],
        [4, 5, 6, 0, 0],
        [0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0],
    ])
    result = pad_if_needed(diag, 4, 5)
    np.testing.assert_equal(result, expected)


def test_count():
    diagram = [
        [5, 0, 2, 0, 0, 0, 0, 0, 0, 0],
        [1, 0, 0, 2, 0, 0, 0, 0, 0, 1],
        [0, 0, 0, 0, 2, 0, 0, 0, 9, 0],
    ]
    assert count(diagram) == 5
