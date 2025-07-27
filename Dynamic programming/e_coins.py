from collections import deque
import math
import sys

def solve_problem(m, S, coins):
    max_limit = S + 1
    visited = [[False] * max_limit for _ in range(max_limit)]
    queue = deque()
    queue.append((0, 0, 0))  # x, y, num_coins
    visited[0][0] = True

    while queue:
        x, y, num = queue.popleft()
        if x * x + y * y == S * S:
            return num
        for cx, cy in coins:
            nx, ny = x + cx, y + cy
            if nx <= S and ny <= S and not visited[nx][ny]:
                if nx * nx + ny * ny <= S * S:
                    visited[nx][ny] = True
                    queue.append((nx, ny, num + 1))
    return "not possible"

def main():
    input_lines = sys.stdin.read().strip().split('\n')
    idx = 0
    n = int(input_lines[idx])
    idx += 1
    results = []
    for _ in range(n):
        while idx < len(input_lines) and input_lines[idx].strip() == '':
            idx += 1
        m, S = map(int, input_lines[idx].split())
        idx += 1
        coins = []
        for _ in range(m):
            x, y = map(int, input_lines[idx].split())
            coins.append((x, y))
            idx += 1
        results.append(str(solve_problem(m, S, coins)))
    print("\n".join(results))

if __name__ == "__main__":
    main()
