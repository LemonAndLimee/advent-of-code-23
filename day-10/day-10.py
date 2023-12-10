PIPES = ['-', '|', 'L', 'J', 'F', '7']

TRAVERSED = 0
UNTRAVERSED = 1

grid = []
starting_coords = [] #coordinates in the form (row, col)

def check_tile(row, col):
    if grid[row][col] in PIPES:
        return UNTRAVERSED
    else:
        return TRAVERSED

def replace_char(s, index, new_char):
    new_string = s[:index] + new_char + s[index+1:]
    return new_string

def make_move(from_row, from_col, marker):
    
    current_tile = grid[from_row][from_col]
    grid[from_row] = replace_char(grid[from_row], from_col, marker)
    
    #check above: |, L, J
    #check below: |, F, 7
    #check left: -, J, 7
    #check right: -, L, F
    
    new_coords = []
    
    if current_tile == '|' or current_tile == 'L' or current_tile == 'J':
        if check_tile(from_row-1, from_col) != TRAVERSED:
            new_coords = [from_row-1, from_col]
    if current_tile == '|' or current_tile == 'F' or current_tile == '7':
        if check_tile(from_row+1, from_col) != TRAVERSED:
            new_coords = [from_row+1, from_col]
    if current_tile == '-' or current_tile == 'J' or current_tile == '7':
        if check_tile(from_row, from_col-1) != TRAVERSED:
            new_coords = [from_row, from_col-1]
    if current_tile == '-' or current_tile == 'L' or current_tile == 'F':
        if check_tile(from_row, from_col+1) != TRAVERSED:
            new_coords = [from_row, from_col+1]
    
    return new_coords 
    
def start(marker):
    row = starting_coords[0]
    col = starting_coords[1]
    
    grid[row] = replace_char(grid[row], col, marker)
    
    if row > 0 and (grid[row-1][col] == '|' or grid[row-1][col] == 'F' or grid[row-1][col] == '7'):
        return [row-1, col]
    if row < len(grid) - 1 and (grid[row+1][col] == '|' or grid[row+1][col] == 'L' or grid[row+1][col] == 'J'):
        return [row+1, col]
    if col > 0 and (grid[row][col-1] == '-' or grid[row][col-1] == 'F' or grid[row][col-1] == 'L'):
        return [row, col-1]
    if col < len(grid[row]) - 1 and (grid[row][col+1] == '-' or grid[row][col+1] == 'J' or grid[row][col+1] == '7'):
        return [row, col+1]
    

with open("day-10\\input.txt", 'r') as input_file:
    for line in input_file:
        string = line[:-1] if line[-1] == '\n' else line
        grid.append(string)
        if 'S' in line:
            starting_coords.append(len(grid)-1)
            starting_coords.append(line.index('S'))

counter = 0
keep_looping = True
next_move = start('X')

while keep_looping:
    counter += 1
    next_move = make_move(next_move[0], next_move[1], 'X')
    if len(next_move) == 0:
        keep_looping = False

answer = (counter // 2) + (counter % 2)
print(answer)

#for i in range(len(grid)):
    #print(grid[i])