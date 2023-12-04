from input import get_split_input
from collections import namedtuple, defaultdict

TEST_CASE = [
    "467..114..",
    "...*......",
    "..35..633.",
    "......#...",
    "617*......",
    ".....+.58.",
    "..592.....",
    "......755.",
    "...$.*....",
    ".664.598.."
]

TEST_CASE_2 = [
    "..764.400.....",
    ".........*....",
    "...@......513."
]

traversals = [(0, 1), (0, -1), (1, 0), (-1, 0), (1, 1), (-1, 1), (-1, -1), (1, -1)]

Point = namedtuple('Point', ['x', 'y'])

def validate(curr, graph):
    valid = False

    for (x, y) in traversals:
        new = Point(curr.x + x, curr.y + y)

        if new.x < 0 or new.x >= len(graph[0]):
            continue

        if new.y < 0 or new.y >= len(graph):
            continue
        
        char = graph[new.y][new.x]
        if char.isnumeric() or char == '.':
            continue
        
        valid = True

    return valid


def close_gear_symbol(curr, graph):
    for (x, y) in traversals:
        new = Point(curr.x + x, curr.y + y)

        if new.x < 0 or new.x >= len(graph[0]):
            continue

        if new.y < 0 or new.y >= len(graph):
            continue
        
        char = graph[new.y][new.x]
        if char == '*':
            return new
        
    return None


def traverse_gear_symbol(graph):
    gear_to_num = defaultdict(list)

    for y, line in enumerate(graph):
        gear_symbols = set()
        stack = []

        for x, char in enumerate(line):
            if char.isnumeric():
                gear_symbol = close_gear_symbol(Point(x, y), graph)
                if gear_symbol:
                    gear_symbols.add(gear_symbol)

                stack.append(char)
            elif len(stack) > 0:
                for gear in gear_symbols:
                    gear_to_num[gear].append(int(''.join(stack)))
                gear_symbols = set()
                stack = []

        if len(stack) > 0 and len(gear_symbols) > 0:
                for gear in gear_symbols:
                    gear_to_num[gear].append(int(''.join(stack)))

    return gear_to_num

def traverse(graph):
    valid_part_nums = []

    for y, line in enumerate(graph):
        is_part_number = False
        stack = []

        for x, char in enumerate(line):
            if char.isnumeric():
                is_part_number = is_part_number or validate(Point(x, y), graph)
                stack.append(char)
            elif len(stack) > 0:
                if is_part_number:
                    valid_part_nums.append(int(''.join(stack)))
                is_part_number = False
                stack = []

        if len(stack) > 0 and is_part_number:
            valid_part_nums.append(int(''.join(stack)))


    return valid_part_nums


def part_one():
    valid_part_nums = traverse(get_split_input(3))
    return sum(valid_part_nums)

def part_two():
    gear_to_num = traverse_gear_symbol(get_split_input(3))

    valid = [nums[0] * nums[1] for (gear, nums) in gear_to_num.items() if len(nums) == 2]
    return sum(valid)

def solution():
    schema = get_split_input(3)


print(part_two())
