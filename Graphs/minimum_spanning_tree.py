class DSU:
    def __init__(self, n):
        self.parent = list(range(n))
        self.rank = [0]*n

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x, y):
        xr = self.find(x)
        yr = self.find(y)
        if xr == yr:
            return False
        if self.rank[xr] < self.rank[yr]:
            self.parent[xr] = yr
        else:
            self.parent[yr] = xr
            if self.rank[xr] == self.rank[yr]:
                self.rank[xr] += 1
        return True

import sys
input = sys.stdin.read
lines = input().splitlines()

i = 0
while i < len(lines):
    if lines[i].strip() == "0 0":
        break

    n, m = map(int, lines[i].split())
    i += 1

    edges = []
    for _ in range(m):
        u, v, w = map(int, lines[i].split())
        if u > v:
            u, v = v, u
        edges.append((w, u, v))
        i += 1

    edges.sort()
    dsu = DSU(n)
    mst_cost = 0
    mst_edges = []

    for w, u, v in edges:
        if dsu.union(u, v):
            mst_cost += w
            mst_edges.append((u, v))

    if len(mst_edges) != n - 1:
        print("Impossible")
    else:
        print(mst_cost)
        mst_edges.sort()
        for u, v in mst_edges:
            print(u, v)
