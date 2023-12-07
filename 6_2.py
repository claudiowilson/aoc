from input import get_split_input

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

    time = int(''.join(lines[0][lines[0].index(':') + 1:].split()))
    distance = int(''.join(lines[1][lines[1].index(':') + 1:].split()))
    
    return find_ways(time, distance)

print(solution())
