import heapq
import sys

input = sys.stdin.read
data = input().splitlines()

i = 0
while True:
    if i >= len(data):
        break

    line = data[i].strip()
    if line == "0 0 0 0":
        break

    n, m, q, s = map(int, line.split())
    i += 1

    graph = [[] for _ in range(n)]
    for _ in range(m):
        u, v, w = map(int, data[i].split())
        graph[u].append((v, w))
        i += 1

    # Dijkstra's algorithm
    dist = [float('inf')] * n
    dist[s] = 0
    pq = [(0, s)]

    while pq:
        d, u = heapq.heappop(pq)
        if d > dist[u]:
            continue
        for v, w in graph[u]:
            if dist[v] > dist[u] + w:
                dist[v] = dist[u] + w
                heapq.heappush(pq, (dist[v], v))

    for _ in range(q):
        target = int(data[i])
        i += 1
        if dist[target] == float('inf'):
            print("Impossible")
        else:
            print(dist[target])
    print()
