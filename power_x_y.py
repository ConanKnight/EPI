from test_framework import generic_test


def power(x, y):
    # TODO - you fill in here.
    # return 0.0
    result = 1.0
    if y < 0:
        x, y = 1/x, -y
    while y:
        if y & 1:
            # y >>= 1
            result *= x
        x, y = x*x, y >> 1
        # print(y)

    return result


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("power_x_y.py", 'power_x_y.tsv', power))
