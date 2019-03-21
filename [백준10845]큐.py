import sys
sys.stdin = open('10845.txt', 'r')

ACT = []
for n in range(int(input())):
    ACT.append(list(input().split()))

q = []
for act in ACT:
    if len(act) == 2:
        q.append(int(act[1]))
    else:
        if act[0] == 'front':
            if q == []:
                print(-1)
            else:
                print(q[0])

        if act[0] == 'back':
            if q == []:
                print(-1)
            else:
                print(q[-1])

        if act[0] == 'size':
            print(len(q))

        if act[0] == 'empty':
            if q == []:
                print(1)
            else:
                print(0)

        if act[0] == 'pop':
            if q == []:
                print(-1)
            else:
                print(q.pop(0))
