def longest_subarray(A):
    largest = 0
    curr = 1
    for i in range(len(A)-1):
        if A[i] == A[i+1]:
            curr += 1
            if curr > largest:
                largest = curr
        else:
            curr = 1
    return largest


longest_subarray([1, 2, 2, 2, 3, 4, 4, 4, 7, 8, 8, 8, 8, 8, 8])
