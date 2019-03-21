import sys
from collections import deque
sys.stdin = open('16954.txt', 'r')

maze = [list(input()) for _ in range(8)]

wall = []
for t in range(8):
    for i in range(8):
        for j in range(8):
            if i + t < 8:
                if maze[i][j] == '#':
                    wall.append([i + t, j, t])

dx = [-1, -1, 0, 1, 1, 1, 0, -1, 0]
dy = [0, 1, 1, 1, 0, -1, -1, -1, 0]
ans = 1
Q = deque()
Q.append([7, 0, 0])
while True:
    s = Q.popleft()
    if s in wall:
        pass
    else:
        for d in range(9):
            x = s[0] + dx[d]
            y = s[1] + dy[d]
            if 0 <= x < 8 and 0 <= y < 8:
                if [x, y, s[2]] not in wall:
                    nt = s[2] + 1
                    Q.append([x, y, nt])

    if s[2] - 1 >= s[0]:
        break
    if s[2] >= 8:
        break
    if len(Q) == 0:
        ans = 0
        break

print(ans)
