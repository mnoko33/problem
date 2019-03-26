import sys
sys.stdin = open('14891.txt', 'r')

one = input()
two = input()
three = input()
four = input()
K = int(input())


def Gear(Nth, D): # 몇번 째 바퀴를 어느 방향으로 회전 시키는지
    global one
    global two
    global three
    global four

    if Nth == 1:
        if D == 1: # 시계 방향 회전
            tmp = one
            one = one[-1] + one[:7]

            if tmp[2] != two[6]:
                # 반시계 방향 회전
                tmp = two
                two = two[1:] + two[0]

                if tmp[2] != three[6]:
                    tmp = three
                    three = three[-1] + three[:7]

                    if tmp[2] != four[6]:
                        four = four[1:] + four[0]

                        return
                    else:
                        return
                else:
                    return
            else:
                return

        else: # 반시계 방향 회전
            tmp = one
            one = one[1:] + one[0]

            if tmp[2] != two[6]:
                # 시계 방향 회전
                tmp = two
                two = two[-1] + two[:7]

                if tmp[2] != three[6]:
                    tmp = three
                    three = three[1:] + three[0]

                    if tmp[2] != four[6]:
                        four = four[-1] + four[:7]

                        return
                    else:
                        return
                else:
                    return
            else:
                return

    elif Nth == 2:
        if D == 1:
            tmp = two
            two = two[-1] + two[:7]

            if one[2] != tmp[6]:
                one = one[1:] + one[0]

            if three[6] != tmp[2]:
                tmp = three
                three = three[1:] + three[0]

                if tmp[2] != four[6]:
                    four = four[-1] + four[:7]

            return
        else:
            tmp = two
            two = two[1:] + two[0]

            if one[2] != tmp[6]:
                one = one[-1] + one[:7]

            if three[6] != tmp[2]:
                tmp = three
                three = three[-1] + three[:7]

                if tmp[2] != four[6]:
                    four = four[1:] + four[0]

            return

    elif Nth == 3:
        if D == 1:
            tmp = three
            three = three[-1] + three[:7]

            if two[2] != tmp[6]:
                ttmp = two
                two = two[1:] + two[0]

                if ttmp[6] != one[2]:
                    one = one[-1] + one[:7]

            if tmp[2] != four[6]:
                four = four[1:] + four[0]

        else:
            tmp = three
            three = three[1:] + three[0]

            if two[2] != tmp[6]:
                ttmp = two
                two = two[-1] + two[:7]

                if ttmp[6] != one[2]:
                    one = one[1:] + one[0]

            if tmp[2] != four[6]:
                four = four[-1] + four[:7]


    elif Nth == 4:
        if D == 1:  # 시계 방향 회전
            tmp = four
            four = four[-1] + four[:7]

            if three[2] != tmp[6]:
                # 반시계 방향 회전
                tmp = three
                three = three[1:] + three[0]

                if two[2] != tmp[6]:
                    tmp = two
                    two = two[-1] + two[:7]

                    if one[2] != tmp[6]:
                        one = one[1:] + one[0]

                        return
                    else:
                        return
                else:
                    return
            else:
                return

        else:  # 반시계 방향 회전
            tmp = four
            four = four[1:] + four[0]

            if three[2] != tmp[6]:
                # 시계 방향 회전
                tmp = three
                three = three[-1] + three[:7]

                if two[2] != tmp[6]:
                    tmp = two
                    two = two[1:] + two[0]

                    if one[2] != tmp[6]:
                        one = one[-1] + one[:7]

                        return
                    else:
                        return
                else:
                    return
            else:
                return


for _ in range(K):
    nth, d = map(int, input().split())
    Gear(nth, d)
if one[0] == '0':
    ONE = 0
else:
    ONE = 1
if two[0] == '0':
    TWO = 0
else:
    TWO = 2
if three[0] == '0':
    THREE = 0
else:
    THREE = 4
if four[0] == '0':
    FOUR = 0
else:
    FOUR = 8
print(ONE + TWO + THREE + FOUR)