import sys
from collections import deque

class MaxFlow:
    def __init__(self, N):
        self.size = N
        self.graph = [[] for _ in range(N)]
        self.level = [0] * N
        self.ptr = [0] * N
        self.INF = float('inf')

    def add_edge(self, u, v, capacity):
        self.graph[u].append([v, capacity, len(self.graph[v])])
        self.graph[v].append([u, 0, len(self.graph[u]) - 1])

    def bfs(self, s, t):
        self.level = [-1] * self.size
        q = deque([s])
        self.level[s] = 0
        while q:
            u = q.popleft()
            for v, cap, _ in self.graph[u]:
                if cap > 0 and self.level[v] == -1:
                    self.level[v] = self.level[u] + 1
                    q.append(v)
        return self.level[t] != -1

    def dfs(self, u, t, flow):
        if u == t or flow == 0:
            return flow
        for i in range(self.ptr[u], len(self.graph[u])):
            v, cap, rev = self.graph[u][i]
            if self.level[v] == self.level[u] + 1 and cap > 0:
                pushed = self.dfs(v, t, min(flow, cap))
                if pushed > 0:
                    self.graph[u][i][1] -= pushed
                    self.graph[v][rev][1] += pushed
                    return pushed
            self.ptr[u] += 1
        return 0

    def dinic(self, s, t):
        flow = 0
        while self.bfs(s, t):
            self.ptr = [0] * self.size
            while True:
                pushed = self.dfs(s, t, self.INF)
                if pushed == 0:
                    break
                flow += pushed
        return flow


def solve():
    try:
        R, C = map(int, sys.stdin.readline().split())
        costs = [list(map(int, sys.stdin.readline().split())) for _ in range(R)]
        castle_r, castle_c = map(int, sys.stdin.readline().split())
    except (IOError, ValueError):
        return

    num_nodes = 2 * R * C + 2
    S = 2 * R * C  # Source node
    T = 2 * R * C + 1  # Sink node
    
    mf = MaxFlow(num_nodes)
    inf = float('inf')

    def in_node(r, c):
        return 2 * (r * C + c)
    def out_node(r, c):
        return 2 * (r * C + c) + 1

    for r in range(R):
        for c in range(C):
            cost = costs[r][c]
            if cost == 0:
                continue

            u_in = in_node(r, c)
            u_out = out_node(r, c)
            
            mf.add_edge(u_in, u_out, cost)

            if r == 0 or r == R - 1 or c == 0 or c == C - 1:
                mf.add_edge(S, u_in, inf)

            if r == castle_r and c == castle_c:
                mf.add_edge(u_out, T, inf)

            for dr, dc in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                nr, nc = r + dr, c + dc
                if 0 <= nr < R and 0 <= nc < C and costs[nr][nc] > 0:
                    v_in = in_node(nr, nc)
                    mf.add_edge(u_out, v_in, inf)

    min_army = mf.dinic(S, T)
    print(min_army)

if __name__ == "__main__":
    solve()