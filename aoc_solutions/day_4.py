from typing import Optional, Literal
import pandas as pd
from aoc_solutions.tools import PuzzleExt, test_and_submit


def score_if_won(board: pd.DataFrame) -> Optional[int]:
    negs = board < 0
    if negs.all(axis=1).any() or negs.all(axis=0).any():
        return int(board[~negs].sum().sum())


def score_of_winning_board(lines, which: Literal['first', 'last']) -> int:
    nums = [int(n) for n in lines[0].split(",")]
    df = lines[1:].str.replace(r"\s+", " ", regex=True).str.strip().str.split(" ", expand=True).dropna(axis=0).astype(int)
    boards = [df[i:i + 5].reset_index(drop=True) for i in range(0, len(df), 5)]
    for board in boards:
        board.won = False
    for num in nums:
        for board in boards:
            if not board.won and num in board.values:
                board.mask(board == num, -99999 if num == 0 else -num, inplace=True)
                if (score := score_if_won(board)) is not None:
                    board.won = True
                    if which == 'first':
                        return score * num
                    if len(remaining := [b for b in boards if not b.won]) == 0:
                        return score * num


def solve_part_one(lines: pd.Series) -> int:
    return score_of_winning_board(lines, 'first')


def solve_part_two(lines: pd.Series) -> int:
    return score_of_winning_board(lines, 'last')


if __name__ == '__main__':
    puzzle = PuzzleExt()
    example_data = puzzle.example_data_str_series
    real_data = puzzle.input_data_str_series
    test_and_submit(puzzle, solve_part_one, solve_part_two, example_data, real_data)
