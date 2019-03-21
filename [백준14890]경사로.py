import sys
sys.stdin = open('14890.txt', 'r')

N, L = map(int, input().split())
ROAD = [list(map(int, input().split())) for _ in range(N)]
road = 0

# for i in range(N):
#     if len(list(set(ROAD[i]))) == 1:
#         road += 1
#
# for j in range(N):
#     cnt = True
#     for i in range(N):
#         if ROAD[i][j] != ROAD[0][j]:
#             cnt = False
#             break
#     if cnt == True:
#         road += 1
row_s = [[i, 0] for i in range(N)]
col_s = [[0, j] for j in range(N)]

def R(s):
    x, y = s[0], s[1]
    if x == 0:
        d = []
    h = ROAD[x][y]
    while True:
