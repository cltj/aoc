import aoc_helper
from aoc_helper import map


raw = aoc_helper.fetch(7, 2024)


def parse_raw(raw: str):
    lines = raw.splitlines()
    parsed_data = []
    for line in lines:
        if line.strip():  # Ensure the line is not empty
            test_value, numbers = line.split(":")
            test_value = int(test_value.strip())
            numbers_tuple = tuple(map(int, numbers.strip().split()))
            parsed_data.append((test_value, numbers_tuple))
    return parsed_data


data = parse_raw(raw)


def evaluate(test_value, numbers):
    def helper(numbers, current_value):
        if not numbers:
            return current_value == test_value

        next_value = numbers[0]
        remaining_numbers = numbers[1:]

        # Try addition
        if helper(remaining_numbers, current_value + next_value):
            return True

        # Try multiplication
        if helper(remaining_numbers, current_value * next_value):
            return True

        # Try concatenation
        concatenated_value = int(str(current_value) + str(next_value))
        if helper(remaining_numbers, concatenated_value):
            return True

        return False

    return helper(numbers[1:], numbers[0])


def part_one(data):
    valid_test_values = [
        test_value for test_value, numbers in data if evaluate(test_value, numbers)
    ]
    print("Valid test values:", valid_test_values)
    return sum(valid_test_values)


def part_two(data=data):
    valid_test_values = [
        test_value for test_value, numbers in data if evaluate(test_value, numbers)
    ]
    print("Valid test values:", valid_test_values)
    return sum(valid_test_values)


aoc_helper.lazy_test(day=7, year=2024, parse=parse_raw, solution=part_one)
aoc_helper.lazy_test(day=7, year=2024, parse=parse_raw, solution=part_two)

aoc_helper.lazy_submit(day=7, year=2024, solution=part_one, data=data)
aoc_helper.lazy_submit(day=7, year=2024, solution=part_two, data=data)
