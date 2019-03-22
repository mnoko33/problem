import sys
sys.stdin = open('14890.txt', 'r')

N, L = map(int, input().split())
ROAD = [list(map(int, input().split())) for _ in range(N)]
for i in range(N):
    for j in range(N):
        tmp = ROAD[i][j]
        ROAD[i][j] = [tmp, 0, 0]
cnt = 0
for k in range(N):
    x, y = 0, k
    while True:
        nx, ny = x + 1, k
        if nx >= N:
            cnt += 1
            # print()
            # print(f'-----세로로 볼 때-----')
            # print()
            # print(f'좌표: 0, {k} 성공')
            break
        # 높이가 같을 때
        if ROAD[x][y][0] == ROAD[nx][ny][0]:
            x, y = nx, ny
        # 오르막일 때
        elif ROAD[x][y][0] + 1 == ROAD[nx][ny][0]:
            # 경사로 설치 검사
            if x - L + 1 >= 0:
                check = True
                for idx in range(L):
                    # 경사로를 놓을 수 있는지 여부
                    if ROAD[x][y][0] != ROAD[x - idx][y][0]:
                        check = False
                        break
                    # 이미 경사로가 설치되어 있는지 여부
                    if ROAD[x - idx][y][1] != 0:
                        check = False
                        break
                    else:
                        ROAD[x - idx][y][1] = 1
                if check == False:
                    break
            else:
                break
            x, y = nx, ny
        # 내리막일 때
        elif ROAD[x][y][0] - 1 == ROAD[nx][ny][0]:
            # 경사로 설치 검사
            if x + L <= N - 1:
                check = True
                for idx in range(1, L + 1):
                    # 경사로를 설치할 수 있는지 여부
                    if ROAD[x][y][0] - 1 != ROAD[x + idx][y][0]:
                        check = False
                        break
                    # 이미 경사로가 설치되어 있는지 여부
                    if ROAD[x + idx][y][1] != 0:
                        check = False
                        break
                    else:
                        ROAD[x + idx][y][1] = 1
                if check == False:
                    break
            else:
                break
            x, y = x + L, y
        else:
            break

    x, y = k, 0
    while True:
        nx, ny = k, y + 1
        if ny >= N:
            # print()
            # print(f'-----가로로 볼 때-----')
            # print()
            # print(f'좌표: {k}, 0 성공')
            cnt += 1
            break
        # 높이가 같을 때
        if ROAD[x][y][0] == ROAD[nx][ny][0]:
            x, y = nx, ny
        # 오르막일 때
        elif ROAD[x][y][0] + 1 == ROAD[nx][ny][0]:
            # 경사로 설치 검사
            if y - L + 1 >= 0:
                check = True
                for idx in range(L):
                    # 경사로를 놓을 수 있는지 여부
                    if ROAD[x][y][0] != ROAD[x][y - idx][0]:
                        check = False
                        break
                    # 이미 경사로가 설치되어 있는지 여부
                    if ROAD[x][y - idx][2] != 0:
                        check = False
                        break
                    else:
                        ROAD[x][y - idx][2] = 1
                if check == False:
                    break
            else:
                break
            x, y = nx, ny
        # 내리막일 때
        elif ROAD[x][y][0] - 1 == ROAD[nx][ny][0]:
            # 경사로 설치 검사
            if y + L <= N - 1:
                check = True
                for idx in range(1, L + 1):
                    # 경사로를 설치할 수 있는지 여부
                    if ROAD[x][y][0] - 1 != ROAD[x][y + idx][0]:
                        check = False
                        break
                    # 이미 경사로가 설치되어 있는지 여부
                    if ROAD[x][y + idx][2] != 0:
                        check = False
                        break
                    else:
                        ROAD[x][y + idx][2] = 1
                if check == False:
                    break
            else:
                break
            x, y = x, y + L
        else:
            break

print(cnt)
