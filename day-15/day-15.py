def apply_hash(string):
    if len(string) == 0: return 0
    else:
        current_value = apply_hash(string[:-1])
        current_value += ord(string[-1])
        current_value *= 17
        current_value = current_value % 256
        return current_value

with open("day-15\\test_input.txt", 'r') as input_file:
    line = input_file.readline()
    steps = line[:-1].split(',') if line[:-1] == '\n' else line.split(',')

    total = 0
    for s in steps:
        hash = apply_hash(s)
        print(str(hash) + " on " + s)
        total += hash
        
    print("\nTotal " + str(total))
    