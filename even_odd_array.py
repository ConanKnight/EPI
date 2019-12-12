import collections
import functools

from test_framework import generic_test
from test_framework.test_failure import TestFailure
from test_framework.test_utils import enable_executor_hook


def even_odd(A):
    # TODO - you fill in here.
    # return
    # next_even, next_odd = 0, len(A) - 1
    # while next_even < next_odd:
    #     if A[next_even] % 2 == 0:
    #         next_even += 1
    #     else:
    #         A[next_even], A[next_odd] = A[next_odd], A[next_even]
    #         next_odd -= 1
    # odd, even = 0, 0
    # first, last = 0, len(A) - 1
    # while first < last:
    #     if A[first] % 2 == 0:
    #         first += 1
    #     else:
    #         A[first], A[last] = A[last], A[first]
    #         # first += 1
    #         last -= 1
    if len(A) < 2:
        return A
    first = 0
    last = len(A)-1

    while first <= last:
        if A[first] % 2 == 0:
            first += 1
        else:
            if A[last] % 2 == 1:
                last -= 1
            else:
                A[first], A[last] = A[last], A[first]

        # if A[first] % 2 != 0 and A[last] % 2 == 0:
        #     A[first], A[last] = A[last], A[first]
        # if not A[first] % 2:
        #     first += 1
        # if A[last] % 2:
        #     last -= 1

    return A

    # even, odd = 0, 0
    # while even < len(A) and odd < len(A):
    #     if A[even] % 2 == 0:
    #         if even <= odd:
    #             even += 1
    #         pass
    #     else:
    #         even += 1

    #     if A[odd] % 2 != 0:


@enable_executor_hook
def even_odd_wrapper(executor, A):
    before = collections.Counter(A)

    executor.run(functools.partial(even_odd, A))

    in_odd = False
    for a in A:
        if a % 2 == 0:
            if in_odd:
                raise TestFailure("Even elements appear in odd part")
        else:
            in_odd = True
    after = collections.Counter(A)
    if before != after:
        raise TestFailure("Elements mismatch")


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("even_odd_array.py",
                                       'even_odd_array.tsv', even_odd_wrapper))
