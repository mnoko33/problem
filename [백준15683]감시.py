import sys
from copy import deepcopy
sys.stdin = open('15683.txt', 'r')

N, M = map(int, input().split())
office = [list(map(int, input().split())) for _ in range(N)]
CCTV = []
wall = []
for i in range(N):
    for j in range(M):
        if office[i][j] == 1:
            CCTV.append([i, j, 1])
        if office[i][j] == 2:
            CCTV.append([i, j, 2])
        if office[i][j] == 3:
            CCTV.append([i, j, 3])
        if office[i][j] == 4:
            CCTV.append([i, j, 4])
        if office[i][j] == 5:
            CCTV.append([i, j, 5])
        if office[i][j] == 6:
            wall.append([i, j])

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]


def DFS(i, office):
    global ans
    if i >= len(CCTV):
        # for o in office:
        #     print(o)
        # print()
        cnt = 0
        for x in range(N):
            for y in range(M):
                if office[x][y] == 0:
                    cnt += 1
        ans.append(cnt)
        return

    cctv = CCTV[i]
    x = cctv[0]
    y = cctv[1]
    n = cctv[2]
    if n == 1:
        for d in range(4):
            k = i
            x = cctv[0]
            y = cctv[1]
            n_office = deepcopy(office)
            while True:
                nx = x + dx[d]
                ny = y + dy[d]
                if 0 <= nx < N and 0 <= ny < M:
                    if n_office[nx][ny] != 6:
                        n_office[nx][ny] = 1
                        x = nx
                        y = ny
                    else:
                        break
                else:
                    break
            k += 1
            DFS(k, n_office)
    if n == 2:
        for d in [[1, 3], [0, 2]]:
            k = i
            n_office = deepcopy(office)
            d1 = d[0]
            d2 = d[1]
            x = cctv[0]
            y = cctv[1]
            while True:
                nx = x + dx[d1]
                ny = y + dy[d1]
                if 0 <= nx < N and 0 <= ny < M:
                    if n_office[nx][ny] != 6:
                        n_office[nx][ny] = 1
                        x = nx
                        y = ny
                    else:
                        break
                else:
                    break
            x = cctv[0]
            y = cctv[1]
            while True:
                nx = x + dx[d2]
                ny = y + dy[d2]
                if 0 <= nx < N and 0 <= ny < M:
                    if n_office[nx][ny] != 6:
                        n_office[nx][ny] = 1
                        x = nx
                        y = ny
                    else:
                        break
                else:
                    break
            k += 1
            DFS(k, n_office)

    if n == 3:
        for d in [[1, 2], [2, 3], [3, 0], [0, 1]]:
            k = i
            n_office = deepcopy(office)
            d1 = d[0]
            d2 = d[1]
            x = cctv[0]
            y = cctv[1]
            while True:
                nx = x + dx[d1]
                ny = y + dy[d1]
                if 0 <= nx < N and 0 <= ny < M:
                    if n_office[nx][ny] != 6:
                        n_office[nx][ny] = 1
                        x = nx
                        y = ny
                    else:
                        break
                else:
                    break
            x = cctv[0]
            y = cctv[1]
            while True:
                nx = x + dx[d2]
                ny = y + dy[d2]
                if 0 <= nx < N and 0 <= ny < M:
                    if n_office[nx][ny] != 6:
                        n_office[nx][ny] = 1
                        x = nx
                        y = ny
                    else:
                        break
                else:
                    break
            k += 1
            DFS(k, n_office)
    if n == 4:
        for d in [[1, 2, 3], [2, 3, 0], [3, 0, 1], [0, 1, 2]]:
            k = i
            n_office = deepcopy(office)
            d1 = d[0]
            d2 = d[1]
            d3 = d[2]
            x = cctv[0]
            y = cctv[1]
            while True:
                nx = x + dx[d1]
                ny = y + dy[d1]
                if 0 <= nx < N and 0 <= ny < M:
                    if n_office[nx][ny] != 6:
                        n_office[nx][ny] = 1
                        x = nx
                        y = ny
                    else:
                        break
                else:
                    break
            x = cctv[0]
            y = cctv[1]
            while True:
                nx = x + dx[d2]
                ny = y + dy[d2]
                if 0 <= nx < N and 0 <= ny < M:
                    if n_office[nx][ny] != 6:
                        n_office[nx][ny] = 1
                        x = nx
                        y = ny
                    else:
                        break
                else:
                    break
            x = cctv[0]
            y = cctv[1]
            while True:
                nx = x + dx[d3]
                ny = y + dy[d3]
                if 0 <= nx < N and 0 <= ny < M:
                    if n_office[nx][ny] != 6:
                        n_office[nx][ny] = 1
                        x = nx
                        y = ny
                    else:
                        break
                else:
                    break
            k += 1
            DFS(k, n_office)

    if n == 5:
        n_office = deepcopy(office)
        x = cctv[0]
        y = cctv[1]
        while True:
            nx = x + dx[0]
            ny = y + dy[0]
            if 0 <= nx < N and 0 <= ny < M:
                if n_office[nx][ny] != 6:
                    n_office[nx][ny] = 1
                    x = nx
                    y = ny
                else:
                    break
            else:
                break
        x = cctv[0]
        y = cctv[1]
        while True:
            nx = x + dx[1]
            ny = y + dy[1]
            if 0 <= nx < N and 0 <= ny < M:
                if n_office[nx][ny] != 6:
                    n_office[nx][ny] = 1
                    x = nx
                    y = ny
                else:
                    break
            else:
                break
        x = cctv[0]
        y = cctv[1]
        while True:
            nx = x + dx[2]
            ny = y + dy[2]
            if 0 <= nx < N and 0 <= ny < M:
                if n_office[nx][ny] != 6:
                    n_office[nx][ny] = 1
                    x = nx
                    y = ny
                else:
                    break
            else:
                break
        x = cctv[0]
        y = cctv[1]
        while True:
            nx = x + dx[3]
            ny = y + dy[3]
            if 0 <= nx < N and 0 <= ny < M:
                if n_office[nx][ny] != 6:
                    n_office[nx][ny] = 1
                    x = nx
                    y = ny
                else:
                    break
            else:
                break
        i += 1
        DFS(i, n_office)
ans = []
i = 0
DFS(i, office)
print(min(ans))

# N, M = map(int, input().split())
# office = [list(map(int, input().split())) for _ in range(N)]
# CCTV = []
# wall = []
# for i in range(N):
#     for j in range(M):
#         if office[i][j] == 1:
#             CCTV.append([i, j, 1])
#         if office[i][j] == 2:
#             CCTV.append([i, j, 2])
#         if office[i][j] == 3:
#             CCTV.append([i, j, 3])
#         if office[i][j] == 4:
#             CCTV.append([i, j, 4])
#         if office[i][j] == 5:
#             CCTV.append([i, j, 5])
#         if office[i][j] == 6:
#             wall.append([i, j])
#
# dx = [-1, 0, 1, 0]
# dy = [0, 1, 0, -1]
# possible = []
#
# def DFS(cctv, d):
#     x = cctv[0]
#     y = cctv[1]
#     nx = x + dx[d]
#     ny = y + dy[d]
#     if 0 <= nx < N and 0 <= ny < M:
#         if [nx, ny] not in wall:
#             possible.append([nx, ny])
#             ncctv = [nx, ny]
#             DFS(ncctv, d)
#     return possible
#
# one = []
# two = []
# three = []
# four = []
# five = []
#
# ALL = [[] for _ in range(len(CCTV))]
# for x in range(len(CCTV)):
#     if CCTV[x][2] == 1:
#         possible = []
#         cctv = [CCTV[x][0], CCTV[x][1]]
#         for d in range(4):
#             tmp = DFS(cctv, d)
#             ALL[x].append(tmp)
#             # print('one:', one)
#     if CCTV[x][2] == 2:
#         possible = []
#         cctv = [CCTV[x][0], CCTV[x][1]]
#         for d in [[1, 3], [0, 2]]:
#             d1 = d[0]
#             d2 = d[1]
#             tmp1 = DFS(cctv, d1)
#             tmp2 = DFS(cctv, d2)
#             ALL[x].append(tmp1 + tmp2)
#             # print('two:', two)
#     if CCTV[x][2] == 3:
#         possible = []
#         cctv = [CCTV[x][0], CCTV[x][1]]
#         for d in [[1, 2], [2, 3], [3, 0], [0, 1]]:
#             d1 = d[0]
#             d2 = d[1]
#             tmp1 = DFS(cctv, d1)
#             tmp2 = DFS(cctv, d2)
#             ALL[x].append(tmp1 + tmp2)
#             # print('three:', three)
#     if CCTV[x][2] == 4:
#         possible = []
#         cctv = [CCTV[x][0], CCTV[x][1]]
#         for d in [[1, 2, 3], [2, 3, 0], [3, 0, 1], [0, 1, 2]]:
#             d1 = d[0]
#             d2 = d[1]
#             d3 = d[2]
#             tmp1 = DFS(cctv, d1)
#             tmp2 = DFS(cctv, d2)
#             tmp3 = DFS(cctv, d3)
#             ALL[x].append(tmp1 + tmp2 + tmp3)
#             # print('four:', four)
#     if CCTV[x][2] == 5:
#         possible = []
#         cctv = [CCTV[x][0], CCTV[x][1]]
#         TMP = []
#         for d in range(4):
#             tmp = DFS(cctv, d)
#             TMP.extend(tmp)
#         ALL[x].append(TMP)
#         # print('five:', five)
# print(ALL)
# print(ALL[0])
# print(ALL[1])
# print(ALL[2])
# print(ALL[3])
# print(ALL[4])
# print(ALL[7])
# if one == []:
#     one.append([])
# if two == []:
#     two.append([])
# if three == []:
#     three.append([])
# if four == []:
#     four.append([])
# if five == []:
#     five.append([])
#
# tmp = []
# maxV = 0
# for a in one:
#     for b in two:
#         for c in three:
#             for d in four:
#                 for e in five:
#                     tmp.extend(a)
#                     tmp.extend(b)
#                     tmp.extend(c)
#                     tmp.extend(d)
#                     tmp.extend(e)
#                     TMP = []
#                     for t in tmp:
#                         if t not in TMP:
#                             TMP.append(t)
#                     if len(TMP) > maxV:
#                         maxV = len(TMP)
# print(N * M - maxV - len(wall))