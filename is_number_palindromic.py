from test_framework import generic_test


def is_palindrome_number(x):
    # TODO - you fill in here.
    if x < 0:
        return False
    result = 0
    oldx = x
    while x:
        result = result * 10 + x % 10
        x //= 10
    return oldx == result


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("is_number_palindromic.py",
                                       "is_number_palindromic.tsv",
                                       is_palindrome_number))
