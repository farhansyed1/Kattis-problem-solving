from collections import deque

# Performs BFS to find an augmenting path from s to t.
def bfs(capacity, graph, s, t, parent):
    visited = set()
    queue = deque([s])
    visited.add(s)
    while queue:
        u = queue.popleft()
        for v in graph[u]:
            # Proceed only if the edge has remaining capacity and v is unvisited
            if v not in visited and capacity[u][v] > 0:
                visited.add(v)
                parent[v] = u  
                if v == t:     # Stop early if sink is reached
                    return True
                queue.append(v)
    return False  # No augmenting path found

# Implements Edmonds-Karp algorithm to compute max flow
def edmonds_karp(n, graph, capacity, s, t):
    flow = 0
    parent = {}
    while bfs(capacity, graph, s, t, parent):
        path_flow = float('inf')
        v = t
        while v != s:
            u = parent[v]
            path_flow = min(path_flow, capacity[u][v])
            v = u
        v = t
        while v != s:
            u = parent[v]
            capacity[u][v] -= path_flow
            capacity[v][u] += path_flow 
            v = u
        flow += path_flow
    return flow

# After max-flow is computed, find the min-cut side U using BFS
def min_cut(n, graph, capacity, s):
    visited = [False] * n
    queue = deque([s])
    visited[s] = True
    while queue:
        u = queue.popleft()
        for v in graph[u]:
            # Follow only edges with residual capacity
            if not visited[v] and capacity[u][v] > 0:
                visited[v] = True
                queue.append(v)
    # Return all reachable nodes from s in residual graph (this is U)
    return [i for i, vis in enumerate(visited) if vis]

def main():
    # Read n: number of nodes, m: number of edges, s: source, t: sink
    n, m, s, t = map(int, input().split())
    
    # Initialize capacity matrix and adjacency list
    capacity = [[0] * n for _ in range(n)]
    graph = [[] for _ in range(n)]

    # Read all edges and build the graph
    for _ in range(m):
        u, v, w = map(int, input().split())
        capacity[u][v] += w  
        graph[u].append(v)
        graph[v].append(u)   # reverse edge for residual graph

    edmonds_karp(n, graph, capacity, s, t)
    
    U = min_cut(n, graph, capacity, s)
    print(len(U))
    for u in U:
        print(u)

if __name__ == '__main__':
    main()
