from test_framework import generic_test


def can_reach_end(A):
    # TODO - you fill in here.
    # return True
    i, furtherest = 0, A[0]
    step = 0
    # last_idx = len(A) - 1

    # while i <= furtherest and furtherest < len(A)-1:
    #     furtherest = max(furtherest, i + A[i])
    #     i += 1
    # if i <= 1:
    #     return 1
    # if furtherest < len(A) - 1:
    #     return 0
    # else:
    #     return 1 + can_reach_end(A[:i])
    for i in range(1, len(A)):
        if i <= furtherest:
            if A[i]+i > furtherest:
                step += 1
                furtherest = A[i]+i
                if furtherest >= len(A):
                    break
    return step


print(can_reach_end([2, 0, 3, 1, 0, 2, 3, 1, 1, 1]))
# if __name__ == '__main__':
#     exit(
#         generic_test.generic_test_main(
#             "advance_by_offsets.py", "advance_by_offsets.tsv", can_reach_end))
