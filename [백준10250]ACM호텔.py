import sys
sys.stdin = open('10250.txt', 'r')

T = int(input())

for test_case in range(1, 1 + T):
    H, W, N = map(int, input().split())  # H : 호텔 층수  W : 각 층의 방수  N : 몇 번 째 손님

    if N % H == 0:  # 6 의 배수
        x = N // H
        y = H
    else:
        x = N // H + 1
        y = N % H

    ans = ''
    if len(str(x)) == 2:
        ans += str(y) + str(x)
    if len(str(x)) == 1:
        ans += str(y) + '0' + str(x)

    print(ans)



  