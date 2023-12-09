from input import get_split_input
from itertools import cycle

TEST_CASE = """
RL

AAA = (BBB, CCC)
BBB = (DDD, EEE)
CCC = (ZZZ, GGG)
DDD = (DDD, DDD)
EEE = (EEE, EEE)
GGG = (GGG, GGG)
ZZZ = (ZZZ, ZZZ)
""".strip().split('\n')

TEST_CASE2 = """
LLR

AAA = (BBB, BBB)
BBB = (AAA, ZZZ)
ZZZ = (ZZZ, ZZZ)
""".strip().split('\n')


def solution():
    lines = get_split_input(8)
    instructs = lines[0]
    
    graph = {}
    for line in lines[1:]:
        if not line:
            continue
        equals = line.index('=')
        left, right = line[equals + 1:].strip().split(', ')
        node = line[:equals].strip()
        graph[node] = (left[1:], right[0:len(right) - 1])

    steps = 0
    node = 'AAA'
    for instruct in cycle(instructs):
        if instruct == 'L':
            node = graph[node][0]
        else:
            node = graph[node][1]

        steps += 1

        if node == 'ZZZ':
            break
    
    return steps

print(solution())

