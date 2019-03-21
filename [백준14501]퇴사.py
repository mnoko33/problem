import sys
sys.stdin = open('14501.txt', 'r')

N = int(input())
T, P = [0], [0]
for _ in range(N):
    t, p = map(int, input().split())
    T.append(t)
    P.append(p)
profit = [0 for _ in range(N + 1)]

for idx in range(1, N + 1):
    if idx + T[idx] <= N + 1:
        profit[idx] = P[idx]

for d in range(1, N + 1):
    tmp = []
    for i in range(1, d):
        if T[i] + i <= d:
            tmp.append(profit[i])
    if tmp != []:
        profit[d] += max(tmp)

print(max(profit))