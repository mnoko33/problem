import sys
sys.stdin = open('13460.txt', 'r')

N, M = map(int, input().split())
arr = []
for _ in range(N):
    TMP = input()
    l = []
    for tmp in TMP:
        l.append(tmp)
    arr.append(l)

for i in range(N):
    for j in range(M):
        if arr[i][j] == 'R':
            R = [i, j]
        if arr[i][j] == 'R':
            B = [i, j]
        if arr[i][j] == 'R':
            O = [i, j]

dxy = [[-1, 0], [0, 1], [1, 0], [0, -1]]
# 각각 R, B 이 구멍에 들어갔는지
holeR = False
holeB = False
move = ['.', 'O']


def UP():
    global holeB
    global holeR
    if R[0] > B[0]:
        # 파란볼 먼저
        while True:
            x = B[0]
            y = B[1]
            dx = x + dxy[0][0]
            dy = y + dxy[0][1]
            if arr[dx][dy] in move:
                if arr[dx][dy] == move[0]:
                    R[0] = dx
                    R[1] = dy
                if arr[dx][dy] == move[1]:
                    holeB = True
                    break
            else:
                break
        if holeB == True:
            return
        # 빨간볼 다음
        while True:
            x = R[0]
            y = R[1]
            dx = x + dxy[0][0]
            dy = y + dxy[0][1]
            if arr[dx][dy] in move:
                if arr[dx][dy] == move[0]:
                    R[0] = dx
                    R[1] = dy
                if arr[dx][dy] == move[1]:
                    holeR = True
                    break
            else:
                break
    else:
        # 빨간볼 먼저
        while True:
            x = R[0]
            y = R[1]
            dx = x + dxy[0][0]
            dy = y + dxy[0][1]
            if arr[dx][dy] in move:
                if arr[dx][dy] == move[0]:
                    R[0] = dx
                    R[1] = dy
                if arr[dx][dy] == move[1]:
                    holeR = True
                    break
            else:
                break
        if holeR == True:
            return
        # 파란볼 다음
        while True:
            x = B[0]
            y = B[1]
            dx = x + dxy[0][0]
            dy = y + dxy[0][1]
            if arr[dx][dy] in move:
                if arr[dx][dy] == move[0]:
                    R[0] = dx
                    R[1] = dy
                if arr[dx][dy] == move[1]:
                    holeB = True
                    break
            else:
                break


def DOWN():
    global holeB
    global holeR
    if R[0] < B[0]:
        # 파란볼 먼저
        while True:
            x = B[0]
            y = B[1]
            dx = x + dxy[2][0]
            dy = y + dxy[2][1]
            if arr[dx][dy] in move:
                if arr[dx][dy] == move[0]:
                    R[0] = dx
                    R[1] = dy
                if arr[dx][dy] == move[1]:
                    holeB = True
                    break
            else:
                break
        if holeB == True:
            return
        # 빨간볼 다음
        while True:
            x = R[0]
            y = R[1]
            dx = x + dxy[2][0]
            dy = y + dxy[2][1]
            if arr[dx][dy] in move:
                if arr[dx][dy] == move[0]:
                    R[0] = dx
                    R[1] = dy
                if arr[dx][dy] == move[1]:
                    holeR = True
                    break
            else:
                break
    else:
        # 빨간볼 먼저
        while True:
            x = R[0]
            y = R[1]
            dx = x + dxy[2][0]
            dy = y + dxy[2][1]
            if arr[dx][dy] in move:
                if arr[dx][dy] == move[0]:
                    R[0] = dx
                    R[1] = dy
                if arr[dx][dy] == move[1]:
                    holeR = True
                    break
            else:
                break
        if holeR == True:
            return
        # 파란볼 다음
        while True:
            x = B[0]
            y = B[1]
            dx = x + dxy[2][0]
            dy = y + dxy[2][1]
            if arr[dx][dy] in move:
                if arr[dx][dy] == move[0]:
                    R[0] = dx
                    R[1] = dy
                if arr[dx][dy] == move[1]:
                    holeB = True
                    break
            else:
                break


def RIGHT():
    pass


def LEFT():
    pass
