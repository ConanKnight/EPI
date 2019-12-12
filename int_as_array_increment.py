from test_framework import generic_test
import math


def plus_one(A):
    # TODO - you fill in here.
    # return []
    # right = len(A) - 1
    # carry = 1
    # while right >= 0:
    #     if A[right] + carry < 10:
    #         A[right] += carry
    #         break
    #     else:
    #         A[right] = 0
    #         carry = 1
    #         right -= 1
    # if right < 0 and carry == 1:
    #     A.insert(0, 1)
    # return A

    # A[-1] += 1
    # for i in reversed(range(1, len(A))):
    #     if A[i] < 10:
    #         # A[i] += 1
    #         break
    #     else:
    #         A[i] = 0
    #         A[i-1] += 1
    # if A[0] == 10:
    #     A[0] = 1
    #     A.append(0)
    # return A

    A[-1] += 1
    i = len(A) - 1
    while i > 0:

        if A[i] >= 10:
            A[i] -= 10
            A[i-1] += 1
        i -= 1
    if A[0] >= 10:
        A[0] -= 10
        A.insert(0, 1)
    return A


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("int_as_array_increment.py",
                                       "int_as_array_increment.tsv", plus_one))
