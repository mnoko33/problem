import sys
sys.stdin = open('2775.txt', 'r')

T = int(input())

for test_case in range(1, 1 + T):
    k = int(input())
    n = int(input())

    def APARTMENT(k, n):  # k0n 호에 사는 사람들의 수
        if k == 0:
            return n
        else:
            tmp = 0
            for i in range(1, n + 1):
                tmp += APARTMENT(k - 1, i)
            return tmp

    print(APARTMENT(k, n))
