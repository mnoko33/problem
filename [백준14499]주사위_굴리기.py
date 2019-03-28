import sys
sys.stdin = open('14499.txt', 'r')

N, M, x, y, K = map(int, input().split())
MAP = [list(map(int, input().split())) for _ in range(N)]
ORDER = list(map(int, input().split()))
dx = [0, 0, 0, -1, 1]
dy = [0, 1, -1, 0, 0]

cube = [[0] * 3 for _ in range(4)]


def CUBE(n):
    # 동쪽
    if n == 1:
        tmp1 = cube[1].pop(0)
        tmp2 = cube[3].pop(1)
        cube[1].append(tmp2)
        cube[3].insert(1, tmp1)
        return
    # 서쪽
    if n == 2:
        tmp1 = cube[1].pop(2)
        tmp2 = cube[3].pop(1)
        cube[1].insert(0, tmp2)
        cube[3].insert(1, tmp1)
        return
    # 북쪽
    if n == 3:
        cube[3][1], cube[2][1] = cube[2][1], cube[3][1]
        cube[2][1], cube[1][1] = cube[1][1], cube[2][1]
        cube[1][1], cube[0][1] = cube[0][1], cube[1][1]
        return
    # 남쪽
    if n == 4:
        cube[1][1], cube[0][1] = cube[0][1], cube[1][1]
        cube[2][1], cube[1][1] = cube[1][1], cube[2][1]
        cube[3][1], cube[2][1] = cube[2][1], cube[3][1]
        return

for i in ORDER:
    nx = x + dx[i]
    ny = y + dy[i]
    if 0 <= nx < N and 0 <= ny < M:
        CUBE(i)
        if MAP[nx][ny] == 0:
            MAP[nx][ny] = cube[1][1]
            x, y = nx, ny
        else:
            MAP[nx][ny], cube[1][1] = 0, MAP[nx][ny]
            x, y = nx, ny
        print(cube[3][1])