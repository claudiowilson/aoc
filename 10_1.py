from input import get_split_input
from collections import defaultdict, namedtuple
import sys

TEST_CASE = """
.....
.S-7.
.|.|.
.L-J.
.....
""".strip().split('\n')

TEST_CASE2 = """
..F7.
.FJ|.
SJ.L7
|F--J
LJ...
""".strip().split('\n')

Point = namedtuple('Point', ['row', 'col'])

SYMBOL_TO_CONNECTIONS = {
    '-': {'E': ['7', 'J', '-'], 'W': ['L', 'F', '-']},
    '|': {'N': ['F', '7', '|'], 'S': ['J', 'L', '|']}, 
    'L': {'E': ['J', '-', '7'], 'N': ['|', '7', 'F']},
    'J': {'N': ['|', '7', 'F'], 'W': ['-', 'L', 'F']},
    '7': {'S': ['|', 'L', 'J'], 'W': ['-', 'L', 'F']},
    'F': {'S': ['|', 'L', 'J'], 'E': ['-', '7', 'J']},
    'S': {'N': ['|', '7', 'F'], 'S': ['|', 'J', 'L'], 'E': ['-', '7', 'J'], 'W': ['L', 'F', '-']},
    '.': {}
}

DIRECTIONS = {
    'N': (0, -1),
    'S': (0, 1),
    'W': (-1, 0),
    'E': (1, 0)
}

def traverse(graph, curr, visited, dist):
    row_len = len(graph[0])
    col_len = len(graph)


    symbol = graph[curr.col][curr.row]

    for direction, delta in DIRECTIONS.items():
        new = Point(curr.row + delta[0], curr.col + delta[1])

        if new.row == row_len or new.row < 0:
            continue

        if new.col == col_len or new.col < 0:
            continue
        
        new_symbol = graph[new.col][new.row]
        if direction in SYMBOL_TO_CONNECTIONS[symbol] and new_symbol in SYMBOL_TO_CONNECTIONS[symbol][direction] and new not in visited:
            visited[new] = dist  + 1
            traverse(graph, new, visited, dist + 1)

def get_init(graph):
    for row, _ in enumerate(graph):
        for col in range(len(graph[0])):
            if graph[col][row] == 'S':
                return Point(row, col)

sys.setrecursionlimit(1000000)

def solution():
    lines = get_split_input(10)
    
    initial = get_init(lines)
    visited = {initial: 0}
    traverse(lines, initial, visited, 0)

    return len(visited) / 2

print(solution())

