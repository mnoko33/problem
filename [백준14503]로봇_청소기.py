import sys
sys.stdin = open('14503.txt', 'r')

N, M = map(int, input().split())
r, c, d = map(int, input().split())
arr = []
for _ in range(N):
    tmp = list(map(int, input().split()))
    arr.append(tmp)

# 재귀
def AI(s, d):
    r, c = s[0], s[1]
    arr[r][c] = 3  # 현재 위치 청소하기
    if d == 0:
        diff = [[0, -1], [1, 0], [0, 1], [-1, 0]]
    if d == 1:
        diff = [[-1, 0], [0, -1], [1, 0], [0, 1]]
    if d == 2:
        diff = [[0, 1], [-1, 0], [0, -1], [1, 0]]
    if d == 3:
        diff = [[1, 0], [0, 1], [-1, 0], [0, -1]]
    for i in range(4):
        # 반시계 방향으로 돌면서 체크할 위치
        x = r + diff[i][0]
        y = c + diff[i][1]
        # 방향을 바꾸고
        d -= 1
        if d < 0:
            d = 4 - abs(d)
        if d == 4:
            d = 0
        # 체크한 위치가 청소되지 않은 곳이라면
        if arr[x][y] == 0:
            # 해당 위치로 이동
            r, c = x, y
            # 해당 위치를 시작점으로 재귀
            s = (r, c)
            AI(s, d)
            return
    # 방향을 체크했는데 청소할 곳이 없을 때 후진 확인
    x = r + diff[1][0]
    y = c + diff[1][1]
    # 뒤가 벽이 아니라면
    if arr[x][y] != 1:
        r = x
        c = y
        s = (r, c)
        AI(s, d)

s = (r, c)
AI(s, d)
cnt = 0
for i in range(N):
    for j in range(M):
        if arr[i][j] == 3:
            cnt += 1

print(cnt)

# 반복문
# while True:
#     bp = False
#     arr[r][c] = 3
#     if d == 0:
#         diff = [[0, -1], [1, 0], [0, 1], [-1, 0]]
#     if d == 1:
#         diff = [[-1, 0], [0, -1], [1, 0], [0, 1]]
#     if d == 2:
#         diff = [[0, 1], [-1, 0], [0, -1], [1, 0]]
#     if d == 3:
#         diff = [[1, 0], [0, 1], [-1, 0], [0, -1]]
#     for i in range(4):
#         x = r + diff[i][0]
#         y = c + diff[i][1]
#         # 방향 바꾸기
#         d -= 1
#         if d < 0:
#             d = 4 - abs(d)
#         if d == 4:
#             d = 0
#         if arr[x][y] == 0:
#             r = x
#             c = y
#             bp = True
#             break
#     if bp == True:
#         pass
#     else:
#         if d == 4:
#             d = 0
#         if d == 0:
#             diff = [[0, -1], [1, 0], [0, 1], [-1, 0]]
#         if d == 1:
#             diff = [[-1, 0], [0, -1], [1, 0], [0, 1]]
#         if d == 2:
#             diff = [[0, 1], [-1, 0], [0, -1], [1, 0]]
#         if d == 3:
#             diff = [[1, 0], [0, 1], [-1, 0], [0, -1]]
#         x = r + diff[1][0]
#         y = c + diff[1][1]
#         if arr[x][y] != 1:
#             r = x
#             c = y
#         else:
#             break
#
# cnt = 0
# for i in range(N):
#     for j in range(M):
#         if arr[i][j] == 3:
#             cnt += 1
# print(cnt)