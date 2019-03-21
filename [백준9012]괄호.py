import sys
sys.stdin = open('9012.txt', 'r')

T = int(input())
for test_case in range(1, 1 + T):
    arr = []
    tmp = input()
    for t in tmp:
        arr.append(t)

    stack = []
    result = True
    for ar in arr:
        if ar == '(':
            stack.append(ar)
        else:
            if stack == []:
                result = False
                break
            else:
                stack.pop(-1)
    if stack != []:
        result = False
    print('YES') if result == True else print('NO')
