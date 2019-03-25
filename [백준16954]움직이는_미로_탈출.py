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

#
# from copy import deepcopy
# game = []
# for _ in range(8):
#    s = input()
#    game.append(s)
#
# copygame = []
# diff = [(1,0),(0,1),(-1,0),(0,-1),(1,1),(-1,-1),(-1,1),(1,-1), (0, 0)]
# visited = [[False for _in range(8)] for_ in range(8)]
# cnt = 0
# def wuk(x,y,game):
#    global cnt
#    if x == 0 and y == 7:
#        cnt += 1
#        return
#    visited[x][y] = True
#    for (dx, dy) in diff:
#        copygame = deepcopy(game)
#        tx = dx+x
#        ty = dy+y
#        if 0<= tx< 8 and 0<= ty < 8 and visited[tx][ty] == False and copygame[tx][ty] == '.' and copygame[x][y] != '#':
#            copygame.insert(0,'........')
#            del copygame[-1]
#            wuk(tx,ty,copygame)
#            visited[tx][ty] = False
#
#
# wuk(7,0,game)
# if cnt >0:
#    print('1')
# elif cnt == 0:
#    print('0')