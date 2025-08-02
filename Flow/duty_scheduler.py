from collections import deque, defaultdict
import sys

class Edge:
    def __init__(self, to, rev, cap):
        self.to = to
        self.rev = rev
        self.cap = cap

class MaxFlow:
    def __init__(self, N):
        self.size = N
        self.graph = [[] for _ in range(N)]

    def add(self, fr, to, cap):
        forward = Edge(to, len(self.graph[to]), cap)
        backward = Edge(fr, len(self.graph[fr]), 0)
        self.graph[fr].append(forward)
        self.graph[to].append(backward)

    def bfs_level(self, s, t, level):
        queue = deque([s])
        level[s] = 0
        while queue:
            v = queue.popleft()
            for e in self.graph[v]:
                if e.cap > 0 and level[e.to] < 0:
                    level[e.to] = level[v] + 1
                    queue.append(e.to)
        return level[t] != -1

    def dfs_flow(self, level, iter, v, t, upTo):
        if v == t:
            return upTo
        for i in range(iter[v], len(self.graph[v])):
            e = self.graph[v][i]
            if e.cap > 0 and level[v] < level[e.to]:
                d = self.dfs_flow(level, iter, e.to, t, min(upTo, e.cap))
                if d > 0:
                    e.cap -= d
                    self.graph[e.to][e.rev].cap += d
                    return d
            iter[v] += 1
        return 0

    def max_flow(self, s, t):
        flow = 0
        level = [-1] * self.size
        INF = 1 << 30
        while True:
            level = [-1] * self.size
            if not self.bfs_level(s, t, level):
                break
            iter = [0] * self.size
            while True:
                f = self.dfs_flow(level, iter, s, t, INF)
                if f == 0:
                    break
                flow += f
        return flow

def duty_scheduler(m, n, availability):
    def can_assign(limit):
        flow = MaxFlow(V)
        for i in range(m):
            flow.add(S, i, limit)
        for i in range(m):
            for d in ra_days[i]:
                flow.add(i, m + d - 1, 1)
        for d in range(n):
            flow.add(m + d, T, 2)
        return flow.max_flow(S, T) == 2 * n

    def build_assignment():
        flow = MaxFlow(V)
        for i in range(m):
            flow.add(S, i, min_max)
        for i in range(m):
            for d in ra_days[i]:
                flow.add(i, m + d - 1, 1)
        for d in range(n):
            flow.add(m + d, T, 2)
        flow.max_flow(S, T)
        assignments = defaultdict(list)
        for i in range(m):
            for e in flow.graph[i]:
                if m <= e.to < m + n and e.cap == 0:
                    day = e.to - m + 1
                    assignments[day].append(ra_names[i])
        return assignments

    ra_names = []
    ra_days = []

    for line in availability:
        parts = line.split()
        name = parts[0]
        d = int(parts[1])
        days = list(map(int, parts[2:]))
        ra_names.append(name)
        ra_days.append(set(days))

    S = m + n
    T = m + n + 1
    V = m + n + 2

    lo, hi = 1, n
    min_max = n

    while lo <= hi:
        mid = (lo + hi) // 2
        if can_assign(mid):
            min_max = mid
            hi = mid - 1
        else:
            lo = mid + 1

    result = build_assignment()
    print(min_max)
    for day in range(1, n + 1):
        r1, r2 = result[day]
        print(f"Day {day}: {r1} {r2}")

def main():
    input = sys.stdin.read
    data = input().splitlines()
    m, n = map(int, data[0].split())
    availability = data[1:]
    duty_scheduler(m, n, availability)

if __name__ == "__main__":
    main()
