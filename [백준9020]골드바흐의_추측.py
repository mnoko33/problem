import sys
sys.stdin = open('9020.txt', 'r')

from math import gcd

def decimal(N):
    isdecimal = True
    for n in range(1, N):
        if gcd(n, N) != 1:
            isdecimal = False
            break
    if isdecimal == True:
        return 1
    else:
        return 2

def TMP(s):
    return abs(s[0] - s[1])

T = int(input())
for test_case in range(1, 1 + T):
    n = int(input())
    result = []
    for a in range(2, n // 2 + 1):
        b = n - a
        if gcd(a, b) == 1 or a == b:
            if decimal(a) == 1 and decimal(b) == 1:
                result.append((a, b))
    result.sort(key=TMP)

    print(result[0][0], result[0][1])
