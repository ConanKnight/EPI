from test_framework import generic_test


def count_bits(x):
    # TODO - you fill in here.
    cnt = 0
    # print(x)
    while x:
        cnt += x & 1
        x //= 2
    return cnt


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("count_bits.py", 'count_bits.tsv',
                                       count_bits))
