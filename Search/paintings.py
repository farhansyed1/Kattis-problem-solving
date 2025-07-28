from itertools import permutations

def solve_case(N, colors, banned_pairs):
    banned_set = set((a, b) for a, b in banned_pairs) | set((b, a) for a, b in banned_pairs)
    count = 0
    best_order = []

    def dfs(path, used):
        nonlocal count, best_order
        if len(path) == N:
            count += 1
            if not best_order:
                best_order = path[:]
            return
        for i in range(N):
            if not used[i]:
                if path and (path[-1], colors[i]) in banned_set:
                    continue
                used[i] = True
                path.append(colors[i])
                dfs(path, used)
                path.pop()
                used[i] = False

    dfs([], [False]*N)
    return count, best_order

T = int(input())
for _ in range(T):
    N = int(input())
    colors = input().split()
    M = int(input())
    banned_pairs = [tuple(input().split()) for _ in range(M)]
    count, favorite = solve_case(N, colors, banned_pairs)
    print(count)
    print(" ".join(favorite))
