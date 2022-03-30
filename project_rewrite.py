def min(x, y):
    return y if x < y else x


def max(values_list):
    max = values_list[0]
    for value in values_list:
        if value > max:
            max = value
    return max


def len(values_list):
    count = 0
    for item in values_list:
        count += 1
    return count


def multiply(x, y):
    pass


def pow(x, y):
    pass


def divmod(x, y):
    pass


if __name__ == "__main__":
    result = len([-100, 10, -5, 88, 41, 0, -53, 100, 82.5, 100.1, 75])
    print(result)
