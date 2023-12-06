# distance travelled = speed * time
# speed = seconds spent holding the button
# distance = (button time) * (total time - button time), where total time is a constant
# let distance = y, button time = x, and total time = b
# y = x(b-x) = bx - x^2
# let previous record be a constant c
# we need to work out every value of x for which y > c, aka. bx - x^2 > c
# ----
# let bx - x^2 = c, so we can work out where the curve crosses y = c
# -x^2 + bx - c = 0
# the quadratic formula can be used to work out the roots of this equation
# then the number of possible record-beating attempts is equal to the number of integers that exist between the two root values

import math

def calculate_answer(times, distances_records):
    result = 1
    for i in range(len(times)):
        options = calculate_number_of_options(times[i], distances_records[i])
        result *= options
    return result

def calculate_number_of_options(time, record):
    roots = quadratic_formula(time, -record)
    lower_bound = math.ceil(roots[0]) if roots[0] % 1 != 0 else roots[0] + 1
    upper_bound = math.floor(roots[1]) if roots[1] % 1 != 0 else roots[1] - 1
    number_of_options = upper_bound - lower_bound + 1
    return number_of_options

def quadratic_formula(b, c):
    roots = []
    discriminant = math.pow(b, 2) - (4 * -1 * c)
    # if there are two roots (if it only has one solution then it equals the record, and doesn't break it)
    if discriminant > 0:
        x = math.sqrt(discriminant) - b
        x = x / (2*-1)
        roots.append(x)
        x = -(math.sqrt(discriminant)) - b
        x = x / (2*-1)
        roots.append(x)
    return roots

times = [38947970]
distances = [241154910741091]

print(calculate_answer(times, distances))