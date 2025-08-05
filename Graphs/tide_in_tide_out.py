import heapq
from collections import deque

def can_move(f1, c1, f2, c2):
    return c2 - f2 >= 50 and c2 - f1 >= 50 and c1 - f2 >= 50

def solve_case(H, N, M, ceiling, floor):
    INF = float('inf')
    dist = [[INF] * M for _ in range(N)]
    dist[0][0] = 0
    pq = []

    visited = [[False]*M for _ in range(N)]
    q = deque()
    q.append((0, 0))
    visited[0][0] = True
    heapq.heappush(pq, (0, 0, 0))  # (time, r, c)

    while q:
        r, c = q.popleft()
        for dr, dc in [(-1,0), (1,0), (0,-1), (0,1)]:
            nr, nc = r + dr, c + dc
            if 0 <= nr < N and 0 <= nc < M:
                if visited[nr][nc]:
                    continue
                if not can_move(floor[r][c], ceiling[r][c], floor[nr][nc], ceiling[nr][nc]):
                    continue
                if ceiling[nr][nc] - H >= 50:
                    visited[nr][nc] = True
                    dist[nr][nc] = 0
                    heapq.heappush(pq, (0, nr, nc))
                    q.append((nr, nc))

    while pq:
        curr_time, r, c = heapq.heappop(pq)
        if curr_time > dist[r][c]:
            continue
        for dr, dc in [(-1,0), (1,0), (0,-1), (0,1)]:
            nr, nc = r + dr, c + dc
            if not (0 <= nr < N and 0 <= nc < M):
                continue
            if not can_move(floor[r][c], ceiling[r][c], floor[nr][nc], ceiling[nr][nc]):
                continue

            max_floor = max(floor[r][c], floor[nr][nc])
            min_ceiling = ceiling[nr][nc]
            max_water_level = min_ceiling - 50
            wait_time = max((H - max_water_level) / 10.0, curr_time)

            water_level = H - wait_time * 10.0

            if wait_time == 0.0 or water_level - floor[r][c] >= 20:
                move_time = 1.0
            else:
                move_time = 10.0

            total_time = wait_time + move_time
            if dist[nr][nc] > total_time:
                dist[nr][nc] = total_time
                heapq.heappush(pq, (total_time, nr, nc))

    return dist[N-1][M-1]

def main():
    T = int(input())
    for case_num in range(1, T+1):
        H, N, M = map(int, input().split())
        ceiling = [list(map(int, input().split())) for _ in range(N)]
        floor = [list(map(int, input().split())) for _ in range(N)]
        result = solve_case(H, N, M, ceiling, floor)
        print(f"Case #{case_num}: {result:.1f}")

if __name__ == "__main__":
    main()
