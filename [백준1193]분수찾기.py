import sys
sys.stdin = open('1193.txt', 'r')

X = int(input())

def start(n):
    if n == 1:
        return 1
    if n == 2:
        return 2
    if n >= 3:
        return n * (n - 1) / 2 + 1


n = 0
while True:
    n += 1
    if start(n) <= X < start(n + 1):
        break
cnt = int(X - start(n))

if n % 2 == 0:
    a = 1 + cnt
    b = n - cnt
    print(f'{a}/{b}')
else:
    a = n - cnt
    b = 1 + cnt
    print(f'{a}/{b}')