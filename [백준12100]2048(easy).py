import sys
sys.stdin = open('12100.txt', 'r')
from collections import deque
from copy import deepcopy
from itertools import product


N = int(input())
board = [list(map(int, input().split())) for _ in range(N)]


def up(board):
    for j in range(N):
        tmp = []
        for i in range(N):
            if board[i][j] != 0:
                tmp.append(board[i][j])
                board[i][j] = 0
        trash = []
        for idx in range(0, len(tmp) - 1):
            if tmp[idx] == tmp[idx + 1]:
                tmp[idx] *= 2
                tmp[idx + 1] = 0
                trash.insert(0, idx + 1)
        for t in trash:
            tmp.pop(t)
        for x in range(len(tmp)):
            board[x][j] = tmp[x]
    return board


def down(board):
    for j in range(N):
        tmp = []
        for i in range(N-1, -1, -1):
            if board[i][j] != 0:
                tmp.append(board[i][j])
                board[i][j] = 0
        trash = []
        for idx in range(0, len(tmp) - 1):
            if tmp[idx] == tmp[idx + 1]:
                tmp[idx] *= 2
                tmp[idx + 1] = 0
                trash.insert(0, idx + 1)
        for t in trash:
            tmp.pop(t)
        for x in range(len(tmp)):
            board[N - x - 1][j] = tmp[x]
    return board


def right(board):
    for i in range(N):
        tmp = []
        for j in range(N - 1, -1, -1):
            if board[i][j] != 0:
                tmp.append(board[i][j])
                board[i][j] = 0
        trash = []
        for idx in range(0, len(tmp) - 1):
            if tmp[idx] == tmp[idx + 1]:
                tmp[idx] *= 2
                tmp[idx + 1] = 0
                trash.insert(0, idx + 1)
        for t in trash:
            tmp.pop(t)
        for x in range(len(tmp)):
            board[i][N - x - 1] = tmp[x]
    return board


def left(board):
    for i in range(N):
        tmp = []
        for j in range(N):
            if board[i][j] != 0:
                tmp.append(board[i][j])
                board[i][j] = 0
        trash = []
        for idx in range(0, len(tmp) - 1):
            if tmp[idx] == tmp[idx + 1]:
                tmp[idx] *= 2
                tmp[idx + 1] = 0
                trash.insert(0, idx + 1)
        for t in trash:
            tmp.pop(t)
        for x in range(len(tmp)):
            board[i][x] = tmp[x]
    return board

#
# print(left(board))

# maxB = 0
# trial = 0
# Q = deque()
# Q.append(board)
# while True:
#     # print(trial)
#     B = Q.popleft()
#     print(B)
#     for i in range(4):
#         if i == 0:
#             tmpB = deepcopy(B)
#             nB = up(tmpB)
#             for x in range(N):
#                 for y in range(N):
#                     if nB[x][y] > maxB:
#                         maxB = nB[x][y]
#             Q.append(nB)
#             trial += 1
#             print('up')
#             print(nB)
#         if i == 1:
#             tmpB = deepcopy(B)
#             nB = down(tmpB)
#             for x in range(N):
#                 for y in range(N):
#                     if nB[x][y] > maxB:
#                         maxB = nB[x][y]
#             Q.append(nB)
#             trial += 1
#             print('down')
#             print(nB)
#         if i == 2:
#             tmpB = deepcopy(B)
#             nB = right(tmpB)
#             for x in range(N):
#                 for y in range(N):
#                     if nB[x][y] > maxB:
#                         maxB = nB[x][y]
#             Q.append(nB)
#             trial += 1
#             print('right')
#             print(nB)
#         if i == 3:
#             tmpB = deepcopy(B)
#             nB = left(tmpB)
#             for x in range(N):
#                 for y in range(N):
#                     if nB[x][y] > maxB:
#                         maxB = nB[x][y]
#             Q.append(nB)
#             trial += 1
#             print('left')
#             print(nB)
#     print('---------------------------')
#     if trial == 4 ** 5:
#         break
# print(maxB)
m = 0
x = [0, 1, 2, 3]
case = list(product(x, repeat=5))
for c in case:
    B = deepcopy(board)
    for i in range(5):
        if c[i] == 0:
            up(B)
        if c[i] == 1:
            down(B)
        if c[i] == 2:
            left(B)
        if c[i] == 3:
            right(B)
    for i in range(N):
        for j in range(N):
            if B[i][j] > m:
                m = B[i][j]
print(m)