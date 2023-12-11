lines = []

hashes = []

# columns expand to the left
# rows expand below
def get_empty():
    rows_without_hash = []
    cols_without_hash = list(range(len(lines[0])-1))
    rows_columns_with_hash = [[],[]]
    for row in range(len(lines)):
        row_has_hash = False
        for col in range(len(lines[row])):
            if lines[row][col] == '#':
                hashes.append([row,col])
                row_has_hash = True
                if col in cols_without_hash:
                    cols_without_hash.remove(col)
        if not row_has_hash and row not in rows_columns_with_hash[0]:
            rows_without_hash.append(row)
    
    return [rows_without_hash, cols_without_hash]

# params need to be in order, such that r2 >= r1, c2 >= c1
def calculate_added_length(r1, r2, c1, c2, empty_rows, empty_cols):
    added = 0
    for i in range(len(empty_rows)):
        if empty_rows[i] >= r1 and empty_rows[i] < r2:
            added += 1
    for i in range(len(empty_cols)):
        if empty_cols[i]  > c1 and empty_cols[i] <= c2:
            added += 1
    return added

def get_path_length(row1, col1, row2, col2, empty_info):
    result = abs(row2-row1) + abs(col2-col1)
    
    added = calculate_added_length(min(row1, row2), max(row1, row2), min(col1, col2), max(col1, col2), empty_info[0], empty_info[1])
    return result + (added * 999999)

def get_total():
    total = 0
    hash_info = get_empty()
    for i in range(len(hashes)):
        for j in range(i+1, len(hashes)):
            path = get_path_length(hashes[i][0], hashes[i][1], hashes[j][0], hashes[j][1], hash_info)
            #print(str(path))
            total += path
    return total

with open("day-11\\input.txt", 'r') as input_file:
    for line in input_file:
        lines.append(line)

print("total = " + str(get_total()))