from test_framework import generic_test


def multiply(num1, num2):
    # TODO - you fill in here.
    # return []
    sign = -1 if (num1[0] < 0) ^ (num2[0] < 0) else 1
    num1[0], num2[0] = abs(num1[0]), abs(num2[0])
    num3 = [0]*(len(num1)+len(num2))
    for i in reversed(range(len(num1))):
        for j in reversed(range(len(num2))):
            num3[i+j+1] += num1[i]*num2[j]
            num3[i+j] += num3[i+j+1] // 10
            num3[i+j+1] %= 10
    for i in range(len(num3)):
        if num3[i] != 0:
            break
    return [sign*num3[i]] + num3[i+1:]

    # num3 = [0]*(len(num1)+len(num2))
    # for i in reversed(range(len(num1))):
    #     for j in reversed(range(len(num2))):
    #         num3[i+j+1] += num1[i] * num2[j]
    #         num3[i+j] += num3[i+j+1] // 10
    #         num3[i+j+1] %= 10
    # num3
    # num3 = num3[next((i for i, x in enumerate(num3) if x != 0), len(num3)):] or [
    #     0]
    # return num3
    # pos = 0
    # while pos < len(num3):
    #     if num3[pos]:
    #         break
    #     else:
    #         pos += 1
    # if pos < len(num3):
    #     num3[pos] = sign*num3[pos]
    #     return num3[pos:]
    # else:
    #     return [0]
if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("int_as_array_multiply.py",
                                       'int_as_array_multiply.tsv', multiply))
