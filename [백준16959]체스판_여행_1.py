import sys
sys.stdin = open('16959.txt', 'r')
from collections import deque

N = int(input())
chess = [list(map(int, input().split())) for _ in range(N)]
order = [0 for _ in range(1 + N ** 2)]
for n in range(1, 1 + N ** 2):
    for i in range(N):
        for j in range(N):
            if chess[i][j] == n:
                order[n] = [i, j]

# def Choice(s, e, h): # 출발점 도착점 말
#     global cnt
#     # Rook(0) check
#     if s[0] == e[0] or s[1] == e[1]:
#         if h == 0:
#             cnt += 1
#         else:
#             cnt += 2
#         h = 0
#
#     # Bishop(1) check
#     elif abs((s[0] - e[0]) / (s[1] - e[1])) == 1:
#         if h == 1:
#             cnt += 1
#         else:
#             cnt += 2
#         h = 1
#
#     # knight(2) check
#     else:
#         if h == 2:
#             cnt += 1
#         else:
#             cnt += 2
#         h = 2
#
# s = order[1]
# e = order[2]
# if s[0] == e[0] or s[1] == e[1]:
#     h = 0
# elif abs((s[0] - e[0]) / (s[1] - e[1])) == 1:
#     h = 1
# else:
#     h = 2
# cnt = 0
# for idx in range(2, N ** 2):
#     Choice(order[idx], order[idx + 1], h)
#
# print(cnt)
knight = [[-2, 1], [-2, -1], [2, 1], [2, -1], [1, 2], [1, -2], [-1, 2], [-1, -2]]
rook = [[1, 0], [-1, 0], [0, 1], [0, -1]]
bishop = [[1, 1], [-1, -1], [1, -1], [-1, 1]]
move = [knight, rook, bishop]

Q = deque()
def BFS(s, e, h):
    pass

s = order[1]
e = order[2]
if s[0] == e[0] or s[1] == e[1]:
    h = 1
elif abs((s[0] - e[0]) / (s[1] - e[1])) == 1:
    h = 2
else:
    h = 0
for idx in range(1, N ** 2):
    Q = deque()
    s = order[idx]
    e = order[idx + 1]
    BFS(s, e, h)
