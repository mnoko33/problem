import sys
sys.stdin = open('3190.txt', 'r')

N = int(input())
apple = []
for _ in range(int(input())):
    apple.append(list(map(int, input().split())))

X = []
C = []
for _ in range(int(input())):
    x, c = input().split()
    X.append(int(x))
    C.append(c)

d = [(-1, 0), (0, 1), (1, 0), (0, -1)]
# 시작 정보
# 0 = head / -1 = tail
snake = [(1, 1)]
# d 의 idx
direction = [1]
# 시간초
sec = 0
while True:
    sec += 1
    # 현재 head
    x, y = snake[0][0], snake[0][1]
    # 이동한 head
    dx = x + d[direction[0]][0]
    dy = y + d[direction[0]][1]

    # 이동한 위치에 사과가 있을 때
    if [dx, dy] in apple:
        # 사과를 먹는다
        idx = apple.index([dx, dy])
        apple[idx] = [-1, -1]
        snake.insert(0, (dx, dy))
        direction.insert(0, direction[0])

    # 이동한 위치가 벽일 때
    elif 1 > dx or dx > N or 1 > dy or dy > N:
        break

    # 이동한 위치에 자신이 있을 때
    elif (dx, dy) in snake:
        break

    # 그냥 이동
    else:
        snake.insert(0, (dx, dy))
        direction.insert(0, direction[0])
        snake.pop(-1)
        direction.pop(-1)

    # 방향 전환하는 타임일 때
    if sec in X:
        x = X.index(sec)
        if C[x] == 'D':
            direction[0] += 1
            direction[0] = direction[0] % 4
        else:
            direction[0] -= 1
            if direction[0] == -1:
                direction[0] = 3

print(sec)
