import os
import sys
import subprocess


def run_command(command):
    result = subprocess.run(command, shell=True, capture_output=True, text=True)
    if result.returncode != 0:
        print(f"Error running command: {command}")
        print(result.stderr)
        sys.exit(1)
    return result.stdout


def create_aoc_files(day, year):
    base_path = f"src/aoc/{year}/d{day:02d}"
    os.makedirs(base_path, exist_ok=True)

    day_file = os.path.join(base_path, f"day_{day:02d}.py")
    input_file = os.path.join(base_path, "input.txt")
    puzzle_file = os.path.join(base_path, "puzzle.txt")

    template_content = f"""
from collections import Counter, defaultdict, deque

import aoc_helper
from aoc_helper import (
    Grid,
    PrioQueue,
    SparseGrid,
    decode_text,
    extract_ints,
    extract_iranges,
    extract_ranges,
    extract_uints,
    frange,
    irange,
    iter,
    list,
    map,
    multirange,
    range,
    search,
    tail_call,
)

raw = aoc_helper.fetch({day}, {year})


def parse_raw(raw: str):
    return ...


data = parse_raw(raw)


# providing this default is somewhat of a hack - there isn't any other way to
# force type inference to happen, AFAIK - but this won't work with standard
# collections (list, set, dict, tuple)
def part_one(data=data):
    ...


aoc_helper.lazy_test(day={day}, year={year}, parse=parse_raw, solution=part_one)


# providing this default is somewhat of a hack - there isn't any other way to
# force type inference to happen, AFAIK - but this won't work with standard
# collections (list, set, dict, tuple)
def part_two(data=data):
    ...


aoc_helper.lazy_test(day={day}, year={year}, parse=parse_raw, solution=part_two)

aoc_helper.lazy_submit(day={day}, year={year}, solution=part_one, data=data)
aoc_helper.lazy_submit(day={day}, year={year}, solution=part_two, data=data)
"""

    input_content = run_command(f"aoc fetch {day} --year {year}")
    puzzle_content = run_command(f"aoc read {day} --year {year}")

    with open(day_file, "w") as f:
        f.write(template_content)
    with open(input_file, "w") as f:
        f.write(input_content)
    with open(puzzle_file, "w") as f:
        f.write(puzzle_content)

    print(f"Files created in {base_path}:")
    print(f"  - {day_file}")
    print(f"  - {input_file}")
    print(f"  - {puzzle_file}")


if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python create_aoc_files.py <day-number> <year-number>")
        sys.exit(1)

    day = int(sys.argv[1])
    year = int(sys.argv[2])

    create_aoc_files(day, year)
