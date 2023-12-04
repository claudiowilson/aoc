from input import get_split_input
import re

TEST_ONE = ["1abc2", "pqr3stu8vwx", "a1b2c3d4e5f", "treb7uchet"]
TEST_TWO = ["two1nine", "eightwothree", "abcone2threexyz", "xtwone3four", "4nineeightseven2", "zoneight234", "7pqrstsixteen"]
reg = "(oneight)|(twone)|(threeight)|(fiveight)|(sevenine)|(eightwo)|(eighthree)|(nineight)|(one)|(two)|(three)|(four)|(five)|(six)|(seven)|(eight)|(nine)|(\d)"

first_match_to_digit = {
    'oneight': '1',
    'twone': '2',
    'threeight': '3',
    'fiveight': '5',
    'sevenine': '7',
    'eightwo': '8',
    'eighthree': '8',
    'nineight': '9',
    'one': '1',
    'two': '2',
    'three': '3',
    'four': '4',
    'five': '5',
    'six': '6',
    'seven': '7',
    'eight': '8',
    'nine': '9'
}

second_match_to_digit = {
    'oneight': '8',
    'twone': '1',
    'threeight': '8',
    'fiveight': '8',
    'sevenine': '9',
    'eightwo': '2',
    'eighthree': '3',
    'nineight': '8',
    'one': '1',
    'two': '2',
    'three': '3',
    'four': '4',
    'five': '5',
    'six': '6',
    'seven': '7',
    'eight': '8',
    'nine': '9'
}

def part_one(calibrations):
    values = map(lambda x: "".join(filter(lambda y: y.isdigit(), x)), calibrations)
    filtered_vals = list(filter(lambda x: len(x) >= 1, values))
    solutions = list(map(lambda x: int(x[0] + x[-1]), filtered_vals))
    return sum(solutions)

def convert_first_match_to_digit(match):
    if len(match) == 1 and match.isnumeric():
        return match

    return first_match_to_digit[match]


def convert_second_match_to_digit(match):
    if len(match) == 1 and match.isnumeric():
        return match

    return second_match_to_digit[match]

def get_digits(calibration):
    matches = list(re.finditer(reg, calibration))
    first_match = matches[0].group()
    second_match = matches[-1].group()

    return convert_first_match_to_digit(first_match) + convert_second_match_to_digit(second_match)
    

def part_two(calibrations):
    values = map(lambda x: int(get_digits(x)), calibrations)
    return sum(values)


def solution():
    calibrations = get_split_input(1)
    return part_two(calibrations)
    #return part_one(calibrations)

print(solution())
