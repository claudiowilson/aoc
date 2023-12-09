from input import get_split_input


TEST_CASE = """
0 3 6 9 12 15
1 3 6 10 15 21
10 13 16 21 30 45
""".strip().split('\n')

def get_differences(sequence):
    last = sequence[-1]
    differences = []
    rest = sequence[:len(sequence) - 1]
    for item in rest[::-1]:
        differences.append(last - item)
        last = item
    return differences[::-1]
        
def solution():
    sequences = list(map(lambda x: [int(y) for y in x.split()], get_split_input(9)))

    answer = 0
    for sequence in sequences:
        sequence = sequence[::-1]
        differences = get_differences(sequence)
        last = differences[-1]
        total = last
        
        while not all(item == 0 for item in differences):
            differences = get_differences(differences)
            last = differences[-1]
            total += last

        answer += sequence[-1] + total
    
    return answer


print(solution())
