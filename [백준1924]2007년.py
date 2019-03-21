import sys
sys.stdin = open('1924.txt', 'r')

x, y = map(int, input().split())
arr = []
for m in range(1, 13):
    if m in [1, 3, 5, 7, 8, 10, 12]:
        for d in range(1, 32):
            arr.append((m, d))
    elif m in [4, 6, 9, 11]:
        for d in range(1, 31):
            arr.append((m, d))
    else:
        for d in range(1, 29):
            arr.append((m, d))
n = arr.index((x, y))
n = n + 1
k = n % 7
result = {1: 'MON', 2: 'TUE', 3: 'WED', 4: 'THU', 5: 'FRI', 6: 'SAT', 0: 'SUN'}
print(result[k])


