from input import get_split_input
import re
import math
import collections

TEST_CASE = [
    "Card 1: 41 48 83 86 17 | 83 86  6 31 17  9 48 53",
    "Card 2: 13 32 20 16 61 | 61 30 68 82 17 32 24 19",
    "Card 3:  1 21 53 59 44 | 69 82 63 72 16 21 14  1",
    "Card 4: 41 92 73 84 69 | 59 84 76 51 58  5 54 83",
    "Card 5: 87 83 26 28 32 | 88 30 70 12 93 22 82 36",
    "Card 6: 31 18 13 56 72 | 74 77 10 23 35 67 36 11"
]

def convert_to_nums(nums):
    return [int(num.group()) for num in re.finditer('\d+', nums)]
        
def solution():
    cards = get_split_input(4)
    copies = collections.Counter({k: 1 for k in range(1, len(cards) + 1)})
    
    points = []
    for idx, card in enumerate(cards):
        winners, nums = map(convert_to_nums, card[card.index(':') + 2:].split('|'))
        same = set(winners).intersection(nums)

        if len(same) >= 1:
            points.append(int(math.pow(2, len(same) - 1)))
        else:
            points.append(0)
        
        for i in range(1, len(same) + 1):
            copies[idx + 1 + i] += 1 * copies[idx + 1]

    return sum(points), sum(copies.values())

print(solution())
