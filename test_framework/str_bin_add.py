def str_bin_add(s1, s2):
    if int(s1) < int(s2):
        s1, s2 = s2, s1
    s3 = ''
    carry = 0
    for i in range(len(s1)):
        if i < len(s2):
            if int(s1[-1-i]) + int(s2[-1-i]) + carry < 2:
                s3 = str(int(s1[-1-i]) + int(s2[-1-i]) + carry) + s3
                carry = 0
            else:
                s3 = str(int(s1[-1-i]) + int(s2[-1-i]) + carry - 2) + s3
                carry = 1
        else:
            if int(s1[-1-i]) + carry < 2:
                s3 = s1[:len(s1)-i-1] + \
                    str(int(s2[-1-i]) + int(s2[-1-i]) + carry) \
                    + s3
                carry = 0
                break
            else:
                s3 = str(int(s1[-1-i]) + carry - 2) + s3
                carry = 1
    if carry == 1:
        s3 = '1' + s3
    print(int(s1, 2), '+', int(s2, 2), '=', int(s3, 2))

    return s3


s1 = '11111100111011'
s2 = '11111110'
str_bin_add(s1, s2)
