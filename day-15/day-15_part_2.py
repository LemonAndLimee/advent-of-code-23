def apply_hash(string):
    if len(string) == 0: return 0
    else:
        current_value = apply_hash(string[:-1])
        current_value += ord(string[-1])
        current_value *= 17
        current_value = current_value % 256
        return current_value

boxes = {}

def process_string(string):
    label = ""
    focal_length = 0
    if '=' in string:
        parts = string.split('=')
        label = parts[0]
        focal_length = int(parts[1])
        
        s = label + " " + str(focal_length)
        box = apply_hash(label)
        
        if box in boxes:
            for i in range(len(boxes[box])):
                if label in boxes[box][i]:
                    boxes[box][i] = s
                    return
            # if label not yet in box
            boxes[box].append(s)
        else:
            boxes[box] = [s,]
            
    elif '-' in string:
        label = string[:-1]
        box = apply_hash(label)
        if box in boxes:
            for i in range(len(boxes[box])):
                if label in boxes[box][i]:
                    boxes[box].pop(i)
                    if len(boxes[box]) == 0:
                        del boxes[box]
                    return

def calculate_answer():
    total = 0
    for box in boxes:
        for i in range(len(boxes[box])):
            focal_length = int(boxes[box][i].split()[1])
            power = 1 + box
            power *= i+1
            power *= focal_length
            total += power
    return total

with open("day-15\\input.txt", 'r') as input_file:
    line = input_file.readline()
    steps = line[:-1].split(',') if line[:-1] == '\n' else line.split(',')

    for step in steps:
        process_string(step)
    
    print(calculate_answer())