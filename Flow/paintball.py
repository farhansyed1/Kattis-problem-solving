n, m = map(int, input().split())
graph = [[] for _ in range(n)]

for _ in range(m):
    a, b = map(int, input().split())
    graph[a-1].append(b-1)
    graph[b-1].append(a-1)

for adj in graph:
    adj.sort()

match_to = [-1] * n

def dfs(u, visited):
    for v in graph[u]:
        if not visited[v]:
            visited[v] = True
            if match_to[v] == -1 or dfs(match_to[v], visited):
                match_to[v] = u
                return True
    return False

for u in range(n):
    visited = [False] * n
    if not dfs(u, visited):
        print("Impossible")
        exit()

target = [0] * n
for i in range(n):
    target[match_to[i]] = i + 1

for t in target:
    print(t)
