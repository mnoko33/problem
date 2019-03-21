import sys
from math import gcd
sys.stdin = open('4948.txt', 'r')

#
# def decimal(N):
#     isdecimal = True
#     for n in range(1, N):
#         if gcd(n, N) != 1:
#             isdecimal = False
#             break
#     if isdecimal == True:
#         return 1
#     else:
#         return 2
#
# T = int(input())
# for test_case in range(1, 1 + T):
#     n = int(input())
#     cnt = 0
#     for x in range(n + 1, 2 * n + 1):
#         a = decimal(x)
#         if a == 1:
#             cnt += 1
#     print(cnt)

T = int(input())
for test_case in range(1, 1 + T):
    n = int(input())
    arr = []
    for x in range(n + 1, 2 * n + 1):
        # print(x)
        tmp = 1
        for a in (str(x)):
            tmp *= int(a)
        if gcd(tmp, x) in [1, x]:
            arr.append(x)
    print(len(arr))

trash = input()
