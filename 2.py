from input import get_split_input

VALID_TOTALS = {
    'green': 13,
    'red': 12,
    'blue': 14
}

VALID_SUM = sum(VALID_TOTALS.values())

TEST_SET = [
    'Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green',
    'Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue',
    'Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red',
    'Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red',
    'Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green'
]

def get_totals(balls):
    totals = {
        'green': 0,
        'red': 0,
        'blue': 0
    }

    split_balls = balls.split(', ')

    for split_ball in split_balls:
        amount, color = split_ball.split(' ')
        totals[color] += int(amount)
    
    return totals


def is_set_valid(balls):
    totals = get_totals(balls)
    
    if sum(totals.values()) > VALID_SUM:
        return False

    if totals['green'] > VALID_TOTALS['green']:
        return False

    if totals['red'] > VALID_TOTALS['red']:
        return False

    if totals['blue'] > VALID_TOTALS['blue']:
        return False
    
    return True

def get_min_set(game):
    mins = {
        'green': 0,
        'red': 0,
        'blue': 0
    }
    
    for balls in get_sets(game):
        totals = get_totals(balls)
        mins['green'] = max([mins['green'], totals['green']])
        mins['blue'] = max([mins['blue'], totals['blue']])
        mins['red'] = max([mins['red'], totals['red']])

    return mins

def get_sets(game):
    return game[game.index(':') + 2:].split('; ')

def is_game_valid(game):
    sets = get_sets(game)
    return all(map(is_set_valid, sets))

def part_two(games):
    min_sets = map(get_min_set, games)
    powers = map(lambda x: x['blue'] * x['green'] * x['red'], min_sets)
    return sum(powers)

def part_one(games):
    validity = [False] * len(games)

    for idx, game in enumerate(games):
        validity[idx] = is_game_valid(game)

    return sum([idx + 1 for idx, x in enumerate(validity) if x])


def solution():
    games = get_split_input(2)
    return part_two(games)

print(solution())
