import sys
from copy import deepcopy
sys.stdin = open('14888.txt', 'r')
# 일반적으로 for 문 실행시 시간초과
# from itertools import permutations
# from copy import deepcopy
#
# N = int(input())
# AA = list(map(int, input().split()))
# operator = []
# plus, minus, multi, div = map(int, input().split())
# for _ in range(plus):
#     operator.append(2)
# for _ in range(minus):
#     operator.append(3)
# for _ in range(multi):
#     operator.append(0)
# for _ in range(div):
#     operator.append(1)
# cnt = len(operator)
# operator.sort()
# operator = list(permutations(operator, len(operator)))
#
# top = 0
# bottom = 1000000000000000000
# for oper in operator:
#     oper = list(oper)
#     A = deepcopy(AA)
#
#     for idx in range(cnt):
#         if oper[idx] == 0:
#             A[idx + 1] = A[idx] * A[idx + 1]
#         elif oper[idx] == 1:
#             A[idx + 1] = int(A[idx] / A[idx + 1])
#         elif oper[idx] == 2:
#             A[idx + 1] = A[idx] + A[idx + 1]
#         elif oper[idx] == 3:
#             A[idx + 1] = A[idx] - A[idx + 1]
#
#     if A[-1] > top:
#         top = A[-1]
#     if A[-1] < bottom:
#         bottom = A[-1]
# print(top)
# print(bottom)

N = int(input())
A = list(map(int, input().split()))
operator = list(map(int, input().split()))
result = []
def dfs(i, A, oper):
    if i == N - 1:
        result.append(A[-1])
        return
    tmp_oper = []
    for idx in range(4):
        if oper[idx] != 0:
            tmp_oper.append(idx)
    for o in tmp_oper:
        nA = deepcopy(A)
        noper = deepcopy(oper)
        if o == 0:
            nA[i + 1] += nA[i]
            noper[0] -= 1
            dfs(i + 1, nA, noper)
        elif o == 1:
            nA[i + 1] = nA[i] - nA[i + 1]
            noper[1] -= 1
            dfs(i + 1, nA, noper)
        elif o == 2:
            nA[i + 1] *= nA[i]
            noper[2] -= 1
            dfs(i + 1, nA, noper)
        elif o == 3:
            if nA[i] < 0:
                nA[i + 1] = (abs(nA[i]) // nA[i + 1]) * -1
            else:
                nA[i + 1] = nA[i] // nA[i + 1]
            noper[3] -= 1
            dfs(i + 1, nA, noper)

dfs(0, A, operator)
print(max(result))
print(min(result))