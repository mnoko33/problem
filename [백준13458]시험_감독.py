import sys
sys.stdin = open('13458.txt', 'r')

N = int(input())
space = list(map(int, input().split()))
space.insert(0, 0)
B, C = map(int, input().split())
cnt = N
for i in range(1, N + 1):
    space[i] = space[i] - B
    if space[i] > 0:
        a = space[i] // C
        cnt += a
        b = space[i] % C
        if b > 0:
            cnt += 1
print(cnt)
