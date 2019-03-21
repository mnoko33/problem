import sys
from itertools import combinations
from collections import deque

sys.stdin = open('15686.txt', 'r')

N, M = map(int, input().split())
city = [list(map(int, input().split())) for _ in range(N)]
chicken = []
house = []
for i in range(N):
    for j in range(N):
        if city[i][j] == 2:
            chicken.append([i, j])
        if city[i][j] == 1:
            house.append([i, j])
if M != 1:
    C = list(combinations(chicken, M))
else:
    C = chicken

if M == 1:
    tmp = []
    for c in C:
        ans = 0
        for h in house:
            x = abs(c[0] - h[0]) + abs(c[1] - h[1])
            ans += x
        tmp.append(ans)
    print(min(tmp))
else:
    pans = []
    for c in C:
        ans = 0
        for h in house:
            tmp = []
            for cx in c:
                x = abs(cx[0] - h[0]) + abs(cx[1] - h[1])
                tmp.append(x)
            ans += min(tmp)

        pans.append(ans)
    print(min(pans))

# BFS 로 풀었을 때 시간 초과
# dx = [-1, 0, 1, 0]
# dy = [0, 1, 0, -1]
#
#
# def BFS(s):
#     Q = deque()
#     Q.append(s)
#     distance = [[0 for _ in range(N)] for _ in range(N)]
#     distance[s[0]][s[1]] = 1
#     while True:
#         v = Q.popleft()
#         if len(c) == 1:
#             if v == c:
#                 dis = distance[v[0]][v[1]]
#                 break
#         else:
#             if v in c:
#                 dis = distance[v[0]][v[1]]
#                 break
#
#         for d in range(4):
#             nx = v[0] + dx[d]
#             ny = v[1] + dy[d]
#             if 0 <= nx < N and 0 <= ny < N:
#                 if distance[nx][ny] == 0:
#                     distance[nx][ny] = distance[v[0]][v[1]] + 1
#                     Q.append([nx, ny])
#
#     return dis

# ans = []
# for c in C:
#     chickenD = 0
#     for h in house:
#         d = BFS(h) - 1
#         chickenD += d
#     ans.append(chickenD)
#
# print(min(ans))


