import re

directions = ""
nodes = {}
A_nodes = []
traversals = []

def traverse(starting_node):
    index = 0
    direction_list_length = len(directions)
    node = starting_node
    while node[-1] != 'Z':
        d = directions[index % direction_list_length]
        node = make_move(d, node)
        index += 1
    return index

def make_move(direction, current_node):
    if direction == 'L':
        return nodes[current_node][0]
    elif direction == 'R':
        return nodes[current_node][1]

def greatest_common_divisor(x, y):
    if x == 0: return y
    elif y == 0: return x
    else: return greatest_common_divisor(y, x%y)

def lowest_common_multiple(x, y):
    return (x*y) // greatest_common_divisor(x,y)

# the solution is the lowest common multiple of the number of traversals for each node to complete, as they must all align to end with Z
def calculate_answer(numbers_list):
    result = numbers_list[0]
    for i in range(1, len(numbers_list)):
        result = lowest_common_multiple(numbers_list[i], result)
    return result

with open("day-8\\input.txt", 'r') as input_file:
    directions = input_file.readline()[:-1]
    next(input_file)
    for line in input_file:
        input = re.split(", | = \(|\*|\)\n|\)", line)
        input.pop() #regex split gives extra empty string consistently, so pop it off the end
        nodes[input[0]] = [input[1], input[2]]
        if input[0][-1] == 'A':
            A_nodes.append(input[0])
    for i in range(len(A_nodes)):
        traversals.append(traverse(A_nodes[i]))
    print(calculate_answer(traversals))
