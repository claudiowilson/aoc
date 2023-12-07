from input import get_split_input

TEST_CASE = """Time:      7  15   30
Distance:  9  40  200""".split('\n')


def find_ways(time, distance):
    ways = 0
    hold = 1

    while True:
        if (time - hold) <= 0:
            break 

        if hold * (time - hold) > distance:
            ways +=1

        hold += 1

    return ways

def solution():
    lines = get_split_input(6)

    time = map(int, lines[0][lines[0].index(':') + 1:].split())
    distance = map(int, lines[1][lines[1].index(':') + 1:].split())
    
    total = 1
    for time, distance in zip(time, distance):
        ways = find_ways(time, distance)
        total *= ways

    return total


print(solution())

