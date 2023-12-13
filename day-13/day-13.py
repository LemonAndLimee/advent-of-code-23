# if a potential LoS is found, expand outwards on each row to check it extends to the whole pattern
def compare_columns(los_index, pattern):
    for row in range(len(pattern)):
        x = los_index
        y = x+1
        while x >= 0 and y < len(pattern[row]):
            #print("testing row x y " + str(row) + " " + str(x) + " " + str(y) + "  len= " + str(len(pattern[row])))
            if pattern[row][x] != pattern[row][y]:
                #print("LoS failed at row x y " + str(row) + " " + str(x) + " " + str(y))
                return -1
            x -= 1
            y += 1
    return 0

# returns no. columns to the left of the vertical LoS, or -1 if there is none
def check_for_vertical(pattern, ignore):
    for i in range(len(pattern[0])-1):
        if i+1 == ignore: continue
        if pattern[0][i] == pattern[0][i+1]: #if there is a match on row 0, check all other rows below
            if compare_columns(i, pattern) == 0:
                return i+1
    return -1

def compare_rows(los_index, pattern):
    for col in range(len(pattern[0])):
        x = los_index
        y = x+1
        while x >= 0 and y < len(pattern):
            if pattern[x][col] != pattern[y][col]:
                return -1
            x -= 1
            y += 1
    return 0

def check_for_horizontal(pattern, ignore):
    for row in range(len(pattern)-1):
        if row+1 == ignore: continue
        if pattern[row][0] == pattern[row+1][0]:
            if compare_rows(row, pattern) == 0:
                return row+1
    return -1

def get_pattern_value(pattern, avoid_v, avoid_h):
    answer = check_for_vertical(pattern, avoid_v)
    if answer >= 0:
        return answer
    else:
        answer = check_for_horizontal(pattern, avoid_h)
        if answer >= 0: return 100 * answer
    return -1

def find_new_value(pattern):
    #calculates original line of symmetry, then passes to the check functions to be ignored
    vertical_los = check_for_vertical(pattern, -1)
    horizontal_los = check_for_horizontal(pattern, -1)
    
    new_pattern = []
    for i in range(len(pattern)):
        new_pattern.append(pattern[i])
    
    for row in range(len(pattern)):
        for col in range(len(pattern[row])):
            if pattern[row][col] == '.':
                new_pattern[row] = pattern[row][:col] + "#" + pattern[row][col+1:]
                value = get_pattern_value(new_pattern, vertical_los, horizontal_los)
                if value >= 0:
                    return value
            else:
                new_pattern[row] = pattern[row][:col] + "." + pattern[row][col+1:]
                value = get_pattern_value(new_pattern, vertical_los, horizontal_los)
                if value >= 0:
                    return value
            new_pattern[row] = pattern[row]
    return -1

with open("day-13\\input.txt", 'r') as input_file:
    total = 0
    current_pattern = []
    for line in input_file:
        if line == "\n":
            total += find_new_value(current_pattern)
            #total += get_pattern_value(current_pattern)
            current_pattern = []
        else:
            l = line[:-1] if line[-1] == '\n' else line
            current_pattern.append(l)
    total += find_new_value(current_pattern)
    
    #total += get_pattern_value(current_pattern)
    print(total)

