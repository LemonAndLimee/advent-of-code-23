def get_next_value(seq):
    if len(seq) == 1: return seq[0]
    
    all_zero = True if seq[0] == 0 else False
    differences = []
    
    for i in range(len(seq)-1):
        difference = seq[i+1] - seq[i]
        if all_zero and seq[i+1] != 0: all_zero = False
        differences.append(difference)
    
    if all_zero:
        return 0
    else:
        new_diff = get_next_value(differences)
        new_value = seq[-1] + new_diff
        return new_value

def get_previous_value(seq):
    if len(seq) == 1: return seq[0]
    
    all_zero = True if seq[0] == 0 else False
    differences = []
    
    for i in range(len(seq)-1):
        difference = seq[i+1] - seq[i]
        if all_zero and seq[i+1] != 0: all_zero = False
        differences.append(difference)
    
    if all_zero:
        return 0
    else:
        new_diff = get_previous_value(differences)
        new_value = seq[0] - new_diff
        return new_value

with open("day-9\\input.txt", 'r') as input_file:
    total = 0
    for line in input_file:
        sequence = line.split()
        sequence = list(map(int, sequence))
        total += get_previous_value(sequence)
    print(total)
