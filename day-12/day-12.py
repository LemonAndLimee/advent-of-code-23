# a list in form x, y, z will result in a string of form .*x.*y.*z.*
# discard any . at the start
# recursively try replacing each ? with a ., pruning if proved impossible
# then try replacing with a #

# for part 2, use dynamic programming to store dictionary of previously explored combinations

DP = {}

# returns -1 if a branch is a failure, else returns number of arrangements for the given branch and list of numbers
def solve(row, nums, counting_hashes):
    key = (row, tuple(nums), counting_hashes)
    if key in DP: return DP[key]
    
    numbers = nums.copy()
    
    if len(row) == 0:
        if counting_hashes:
            if len(numbers) > 1: return -1
            if numbers[0] == 0:
                return 1
            else: return -1
        else:
            if len(numbers) > 0: return -1
            return 1
    
    is_counting_hashes = counting_hashes
    if row[0] == '#':
        if not is_counting_hashes: is_counting_hashes = True
        if len(numbers) == 0:
            return -1
        else:
            numbers[0] = numbers[0] - 1
            if numbers[0] < 0: return -1
    elif row[0] == '.':
        if is_counting_hashes:
            is_counting_hashes = False
            if numbers[0] == 0: numbers.pop(0)
            elif numbers[0] > 0: return -1
    
    
    if row[0] != '?':
        answer = solve(row[1:], numbers, is_counting_hashes)
        key = (row[1:], tuple(numbers), is_counting_hashes)
        if key not in DP: DP[key] = answer
        return answer
    
    permutations = 0

    branch1 = solve("." + row[1:], numbers, is_counting_hashes)
    if branch1 >= 0: permutations += branch1
    key = ("." + row[1:], tuple(numbers), is_counting_hashes)
    if key not in DP: DP[key] = branch1
    
    branch2 = solve("#" + row[1:], numbers, is_counting_hashes)
    if branch2 >= 0: permutations += branch2
    key = ("#" + row[1:], tuple(numbers), is_counting_hashes)
    if key not in DP: DP[key] = branch2

    if branch1 <0 and branch2 <0: return -1
    
    return permutations

with open("day-12\\input.txt", 'r') as input_file:
    total = 0
    for line in input_file:
        parts = line.split()
        string = parts[0]
        numbers = parts[1].split(",")
        numbers = list(map(int, numbers))
        
        new_string = string
        for i in range(4):
            new_string = new_string + "?" + string
        numbers = numbers * 5
        
        arrangements = solve(new_string, numbers, False)
        total += arrangements
    
    print(total)