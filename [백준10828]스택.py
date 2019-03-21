import sys
sys.stdin = open('10828.txt', 'r')

N = int(input())
arr = []
for _ in range(N):
    arr.append(list(input().split()))

stack = []
for act in arr:
    if act[0] == 'push':
        stack.append(act[1])
    if act[0] == 'pop':
        if stack != []:
            print(stack.pop(-1))
        else:
            print(-1)
    if act[0] == 'size':
        print(len(stack))
    if act[0] == 'empty':
        if stack == []:
            print(1)
        else:
            print(0)
    if act[0] == 'top':
        if stack == []:
            print(-1)
        else:
            print(stack[-1])
