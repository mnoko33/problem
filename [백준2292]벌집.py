import sys
sys.stdin = open('2292.txt', 'r')

N = int(input())


def BEE(n):
    if n == 1:
        return 1
    if n == 2:
        return 2
    if n >= 3:
        return BEE(n - 1) + 6 * (n - 2)


n = 1
while True:
    if N == 1:
        n = 0
        break
    if BEE(n) <= N < BEE(n + 1):
        break
    n += 1
if N == 1:
    print(1)
else:
    print(n)

