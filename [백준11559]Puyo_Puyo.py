import sys
sys.stdin = open('11559.txt', 'r')
from collections import deque

puyo = []
for _ in range(12):
    tmp = list(' '.join(input().split()))
    puyo.append(tmp)


def Gravitiy():
    for j in range(6):
        for i in range(11, -1, -1):
            while True:
                dx = i + 1
                dy = j
                if dx <= 11:
                    if puyo[dx][dy] == 'X':
                        puyo[i][j], puyo[dx][dy] = puyo[dx][dy], puyo[i][j]
                if dx == 12:
                    break
                i = dx
                j = dy


dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]


def Puyo(s, v):
    Q.append(s)
    while True:
        t = Q.popleft()
        for d in range(4):
            nx = t[0] + dx[d]
            ny = t[1] + dy[d]
            if 0 <= nx < 12 and 0 <= ny < 6:
                if puyo[nx][ny] == v:
                    puyo[nx][ny] = 'X'
                    pl.append([nx, ny])
                    Q.append([nx, ny])
        if len(Q) == 0:
            break


cnt = 0
while True:
    bp = True
    for i in range(12):
        for j in range(6):
            if puyo[i][j] != '.' and puyo[i][j] != 'X':
                v = puyo[i][j]
                puyo[i][j] = 'X'
                s = [i, j]
                pl = [[i, j]]
                Q = deque()
                Puyo(s, v)
                if len(pl) < 4:
                    for x in pl:
                        puyo[x[0]][x[1]] = v
                else:
                    bp = False
    Gravitiy()
    if bp == True:
        break
    else:
        cnt += 1
print(cnt)