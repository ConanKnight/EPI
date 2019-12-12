from test_framework import generic_test


def closest_int_same_bit_count(x):
    # TODO - you fill in here.
    y = x ^ (x >> 1)
    if y != 0:
        z = y & ~(y-1)
        return x ^ (z | z << 1)


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("closest_int_same_weight.py",
                                       "closest_int_same_weight.tsv",
                                       closest_int_same_bit_count))
