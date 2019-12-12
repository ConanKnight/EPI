import functools

from test_framework import generic_test
from test_framework.test_failure import TestFailure
from test_framework.test_utils import enable_executor_hook

RED, WHITE, BLUE = range(3)


def dutch_flag_partition(pivot_index, A):
    # TODO - you fill in here.
    # return
    # left, right = 0, len(A) - 1
    pivot = A[pivot_index]

    small, equal, large = 0, 0, len(A)-1

    while equal <= large:
        if A[equal] < pivot:
            A[small], A[equal] = A[equal], A[small]
            small, equal = small + 1, equal + 1
        elif A[equal] == pivot:
            equal += 1
        else:
            A[equal], A[large] = A[large], A[equal]
            large -= 1

    # i = 0
    # j = len(A)-1
    # while i < j:
    #     if A[i] < pivot:
    #         i += 1
    #     else:
    #         A[i], A[j] = A[j], A[i]
    #         j -= 1
    # # i == j
    # if A[i] < pivot:
    #     i += 1
    #     j += 1
    # while j < len(A):
    #     if A[j] == pivot:
    #         A[i], A[j] = A[j], A[i]
    #         i += 1
    #     j += 1
    # for i in reversed(range(left, len(A))):
    #     if A[i] > pivot:
    #         A[i], A[right] = A[right], A[i]
    #         right -= 1
    # small = []
    # equal = []
    # large = []
    # for i in A:
    #     if i < pivot:
    #         small.append(i)
    #     elif i == pivot:
    #         equal.append(i)
    #     else:
    #         large.append(i)
    # A = small + equal + large
    # print(A)
    # return A
    # small, equal, large = 0, 0, len(A)
    # while equal < large:
    #     if A[equal] < pivot:
    #         A[small], A[equal] = A[equal], A[small]
    #         small += 1
    #         equal += 1
    #     elif A[equal] == pivot:
    #         equal += 1
    #     else:
    #         large -= 1
    #         A[equal], A[large] = A[large], A[equal]

    # left, right = 0, len(A) - 1
    # pivot = A[pivot_index]
    # while left < right:
    #     if A[left] <= pivot:
    #         left += 1
    #     else:
    #         A[left], A[right] = A[right], A[left]
    #         right -= 1
    # newleft = 0
    # newright = left-1 if A[left] > pivot else left
    # while newleft < newright:
    #     # for i in range(left+1):
    #     if A[newleft] < pivot:
    #         newleft += 1
    #     else:
    #         A[newleft], A[newright] = A[newright], A[newleft]
    #         newright -= 1


@enable_executor_hook
def dutch_flag_partition_wrapper(executor, A, pivot_idx):
    count = [0, 0, 0]
    for x in A:
        count[x] += 1
    pivot = A[pivot_idx]

    executor.run(functools.partial(dutch_flag_partition, pivot_idx, A))

    i = 0
    while i < len(A) and A[i] < pivot:
        count[A[i]] -= 1
        i += 1
    while i < len(A) and A[i] == pivot:
        count[A[i]] -= 1
        i += 1
    while i < len(A) and A[i] > pivot:
        count[A[i]] -= 1
        i += 1

    if i != len(A):
        raise TestFailure('Not partitioned after {}th element'.format(i))
    elif any(count):
        raise TestFailure("Some elements are missing from original array")


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("dutch_national_flag.py",
                                       'dutch_national_flag.tsv',
                                       dutch_flag_partition_wrapper))
