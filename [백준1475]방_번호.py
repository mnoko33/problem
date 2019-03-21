import sys
sys.stdin = open('1475.txt', 'r')

N = int(input())
cnt = [0] * 10

for n in str(N):
    cnt[int(n)] += 1

cnt[6] += cnt[9]
cnt[9] = 0
if cnt[6] % 2 == 0:
    cnt[6] = cnt[6] // 2
else:
    cnt[6] = cnt[6] // 2 + 1

print(max(cnt))