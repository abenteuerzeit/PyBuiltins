def min_func(x, y):
    return x if x < y else y


def max_func(values_list):
    max = values_list[0]
    for value in values_list:
        if value > max:
            max = value
    return max


def length(values_list):
    count = 0
    for item in values_list:
        count += 1
    return count


def multiply(x, y):
    if y == 0:
        return 0
    if y > 0:
        return x + multiply(x, y-1)
    if y < 0:
        return -multiply(x, -y)


def power(x, y):
    result = 1
    for i in range(y):
        result *= x
    return result


def div_mod(x, y):
    # doesn't work with negative values
    count = 0
    while x >= y:
        x = x - y
        count += 1
    return count, x
