from test_framework import generic_test


def apply_permutation(perm, A):
    # TODO - you fill in here.
    # B = [0]*len(A)
    # for i in range(len(perm)):
    #     B[perm[i]] = A[i]
    # return B
    for i in range(len(A)):
        while perm[i] != i:
            A[i], A[perm[i]] = A[perm[i]], A[i]
            perm[perm[i]], perm[i] = perm[i], perm[perm[i]]
    # print(A)


def apply_permutation_wrapper(perm, A):
    apply_permutation(perm, A)
    return A


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("apply_permutation.py",
                                       "apply_permutation.tsv",
                                       apply_permutation_wrapper))
