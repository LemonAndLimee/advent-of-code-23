import re

directions = ""
nodes = {}

def traverse():
    index = 0
    direction_list_length = len(directions)
    node = "AAA"
    while node != "ZZZ":
        d = directions[index % direction_list_length]
        node = make_move(d, node)
        index += 1
    return index

def make_move(direction, current_node):
    if direction == 'L':
        return nodes[current_node][0]
    elif direction == 'R':
        return nodes[current_node][1]

with open("day-8\\input.txt", 'r') as input_file:
    directions = input_file.readline()[:-1]
    next(input_file)
    for line in input_file:
        input = re.split(", | = \(|\*|\)\n|\)", line)
        input.pop() #regex split gives extra empty string consistently, so pop it off the end
        nodes[input[0]] = [input[1], input[2]]
    print(traverse())
