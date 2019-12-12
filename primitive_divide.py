from test_framework import generic_test


def divide(x, y):
    # TODO - you fill in here.
    result = 0
    power = 0
    y_power = y
    while y_power <= x:
        y_power <<= 1
        power += 1
    # y_power >>= 1
    # power -= 1
    # print(x < y_power)
    while x >= y:
        while x < y_power:
            y_power >>= 1
            power -= 1
        x -= y_power
        result += (1 << power)
    # while x >= y:
    #     if x >= y_power:
    #         result += 1 << power
    #         x -= y_power
    #     y_power >>= 1
    #     power -= 1

    # y_power = y >> power
    # while x >= y:
    #     while y_power >= x:
    #         power -= 1
    #     x -= y
    #     result += 1
    return result


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("primitive_divide.py",
                                       "primitive_divide.tsv", divide))
