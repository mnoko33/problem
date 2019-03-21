import sys
sys.stdin = open('5188.txt', 'r')

for test_case in range(1, 1 + int(input())):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    for i in range(1, N):
        arr[i][0] += arr[i - 1][0]
    for j in range(1, N):
        arr[0][j] += arr[0][j - 1]
    for i in range(1, N):
        for j in range(1, N):
            arr[i][j] = min(arr[i][j] + arr[i - 1][j], arr[i][j] + arr[i][j - 1])
    print(f'#{test_case} {arr[N - 1][N - 1]}')
