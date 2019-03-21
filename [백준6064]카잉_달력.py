import sys
from math import gcd
sys.stdin = open('6064.txt', 'r')

T = int(input())
for test_case in range(1, 1 + T):
    M, N, x, y = map(int, input().split())
    lcm = int(M * N / gcd(M, N))
    cnt = 1
    a, b = 1, 1

    # while True:     #  a 와 b 를 1 부터 세기 때문에 시간 초과
    #     if a > M:
    #         a = a % M
    #     if b > N:
    #         b = b % N
    #
    #     if (a, b) == (x, y):
    #         break
    #
    #     if cnt > lcm:
    #         cnt = -1
    #         break
    #
    #     cnt += 1
    #     a += 1
    #     b += 1
    # print(cnt)
    n = 1
    result = 0
    while True:
        a = (n - 1) * M + x
        if a > lcm:
            result = -1
            break
        b = a % N
        if b == 0:
            b = N
        if b == y:
            break
        n += 1

    if result == -1:
        print(-1)
    else:
        print(a)



