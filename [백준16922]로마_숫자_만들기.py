import sys
sys.stdin = open('16922.txt', 'r')

N = int(input())
arr = [1, 5, 10, 50]
ans = [1, 5, 10, 50]
cnt = 1

while True:
    tmp = []
    if cnt == N:
        break
    for x in range(4):
        for y in range(len(ans)):
            z = arr[x] + ans[y]
            if z not in tmp:
                tmp.append(z)
    cnt += 1
    ans = tmp

print(len(ans))
