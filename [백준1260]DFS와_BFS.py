import sys
sys.stdin = open('1260.txt', 'r')


def DFS(n):
    visit[n] = True
    print(f'{n}', end=' ')
    for u in G[n]:
        if visit[u] == False:
            DFS(u)

def BFS(n):
    q = [n]
    while True:
        v = q.pop(0)
        if visit[v] == False:
            visit[v] = True
            print(f'{v}', end=' ')
            for u in G[v]:
                if visit[u] == False:
                    q.append(u)
        if q == []:
            break


N, M, V = map(int, input().split())
G = [[] for _ in range(N + 1)]
for _ in range(M):
    s, e = map(int, input().split())
    G[s].append(e)
    G[e].append(s)
for i in range(1, N + 1):
    G[i].sort()

visit = [False for _ in range(N + 1)]
DFS(V)
print()
visit = [False for _ in range(N + 1)]
BFS(V)
