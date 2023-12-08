from input import get_split_input
from collections import Counter

TEST_CASE = """
32T3K 765
T55J5 684
KK677 28
KTJJT 220
QQQJA 483
""".strip().split('\n')

TEST_CASE2 = """
2345A 1
Q2KJJ 13
Q2Q2Q 19
T3T3J 17
T3Q33 11
2345J 3
J345A 2
32T3K 5
T55J5 29
KK677 7
KTJJT 34
QQQJA 31
JJJJJ 37
JAAAA 43
AAAAJ 59
AAAAA 61
2AAAA 23
2JJJJ 53
JJJJ2 41
""".strip().split('\n')

card_to_value = {
    'A': 13,
    'K': 12,
    'Q': 11,
    'T': 10,
    '9': 9,
    '8': 8,
    '7': 7,
    '6': 6,
    '5': 5,
    '4': 4,
    '3': 3,
    '2': 2,
    'J': 1
}

def check_all_possible(hand, test):
    cards = set(hand)
    if 'J' in cards:
        cards.remove('J')

    for idx, c in enumerate(hand):
        if c == 'J':
            for card in cards:
                if test(tuple(hand[0:idx] + tuple(card) + hand[idx + 1:])):
                    return True
    return False

def is_five_of_a_kind(hand):
    if len(set(hand)) == 1:
        return True
    
    return check_all_possible(hand, is_five_of_a_kind)

def is_four_of_a_kind(hand):
    counter = Counter(hand)
    for value, count in counter.most_common(1):
        if count == 4:
            return True

    return check_all_possible(hand, is_four_of_a_kind)

def is_full_house(hand):
    counter = Counter(hand)
    
    if [x[1] for x in counter.most_common(2)] == [3, 2]:
        return True

    return check_all_possible(hand, is_full_house)

def is_three_of_a_kind(hand):
    counter = Counter(hand)
    for value, count in counter.most_common(1):
        if count == 3:
            return True

    return check_all_possible(hand, is_three_of_a_kind)

def is_two_pair(hand):
    counter = Counter(hand)

    if [x[1] for x in counter.most_common(2)] == [2, 2]:
        return True

    return check_all_possible(hand, is_two_pair)

def is_one_pair(hand):
    counter = Counter(hand)
    for value, count in counter.most_common(1):
        if count == 2:
            return True

    return check_all_possible(hand, is_one_pair)

def partition(pred, iterable):
    trues = []
    falses = []
    for item in iterable:
        if pred(item):
            trues.append(item)
        else:
            falses.append(item)
    return trues, falses

def hand_to_value(hand):
    return [card_to_value[card] for card in hand]

def sort_by_highest(hands):
    return sorted(hands, key=lambda x: hand_to_value(x), reverse=True)

def solution():
    hands_and_bids = {tuple(x.split()[0]): int(x.split()[1]) for x in get_split_input(7)}
    hands = [tuple(x) for x in hands_and_bids.keys()]

    five_of_kinds, rest = partition(is_five_of_a_kind, hands)
    four_of_kinds, rest = partition(is_four_of_a_kind, rest)
    full_houses, rest = partition(is_full_house, rest)
    three_of_kinds, rest = partition(is_three_of_a_kind, rest)
    two_pairs, rest = partition(is_two_pair, rest)
    one_pair, rest = partition(is_one_pair, rest)
    high_cards = rest

    print(is_five_of_a_kind(('5', '5', '5', '5', 'J')))
    curr_rank = len(hands)

    total_winnings = 0

    for hand in sort_by_highest(five_of_kinds):
        total_winnings += curr_rank * hands_and_bids[hand]
        curr_rank -= 1
    for hand in sort_by_highest(four_of_kinds):
        total_winnings += curr_rank * hands_and_bids[hand]
        curr_rank -= 1
    for hand in sort_by_highest(full_houses):
        total_winnings += curr_rank * hands_and_bids[hand]
        curr_rank -= 1
    for hand in sort_by_highest(three_of_kinds):
        total_winnings += curr_rank * hands_and_bids[hand]
        curr_rank -= 1
    for hand in sort_by_highest(two_pairs):
        total_winnings += curr_rank * hands_and_bids[hand]
        curr_rank -= 1
    for hand in sort_by_highest(one_pair):
        total_winnings += curr_rank * hands_and_bids[hand]
        curr_rank -= 1
    for hand in sort_by_highest(high_cards):
        total_winnings += curr_rank * hands_and_bids[hand]
        curr_rank -= 1
    
    assert len(hands) == len(five_of_kinds) + len(four_of_kinds) + len(full_houses) + len(three_of_kinds) + len(two_pairs) + len(one_pair) + len(high_cards)
    assert curr_rank == 0

    return total_winnings

print(solution())
