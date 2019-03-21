import sys
sys.stdin = open('15685.txt', 'r')

N = int(input())
X = []
Y = []
D = []
G = []
for _ in range(N):
    x, y, d, g = map(int, input().split())
    X.append(x)  # x 좌표
    Y.append(y)  # y 좌표
    D.append(d)  # 방향
    G.append(g)  # 세대 > 드래곤의 길이

dx = [1, 0, -1, 0]
dy = [0, -1, 0, 1]

dragon = []
direction = []


def Dragon_c(xy, d, g):
    if g == 0:
        dragon.append([xy[0], xy[1]])
        dragon.append([xy[0] + dx[d], xy[1] + dy[d]])
        direction.append(d)
        # print('dragon', dragon)
        # print('direction', direction)
        # print()
        return [dragon, direction]
    if g >= 1:
        D = Dragon_c(xy, d, g - 1)
        ex_dragon = D[0]
        ex_direction = D[1]
        tmp_direction = ex_direction[::-1]
        for d in tmp_direction:
            d += 1
            if d == 4:
                d = 0
            x = ex_dragon[-1][0]
            y = ex_dragon[-1][1]
            ex_dragon.append([x + dx[d], y + dy[d]])
            ex_direction.append(d)
            # print('dragon', ex_dragon)
            # print('direction', ex_direction)
            # print()
        return [ex_dragon, ex_direction]

result = []
for i in range(N):
    # print(f'------dragon {i}-------------')
    dragon = []
    direction = []
    result.extend(Dragon_c([X[i], Y[i]], D[i], G[i])[0])
# print(result)
tmp = []
for r in result:
    if 0 <= r[0] <= 100 and 0 <= r[1] <= 100:
        tmp.append(r)
result = []
for t in tmp:
    if t not in result:
        result.append(t)
cnt = 0
for c in result:
    if [c[0] + 1, c[1] + 1] in result and [c[0] + 1, c[1]] in result and [c[0], c[1] + 1] in result:
        cnt += 1
print(cnt)