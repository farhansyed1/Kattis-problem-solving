import heapq
import sys

def solve_block_crusher():
    try:
        line = sys.stdin.readline()
        if not line: return False
        h, w = map(int, line.split())
    except (IOError, ValueError):
        return False

    if h == 0 and w == 0:
        return False

    grid = [[int(d) for d in sys.stdin.readline().strip()] for _ in range(h)]

    dist = [[float('inf')] * w for _ in range(h)]
    parent = [[None] * w for _ in range(h)]
    pq = []

    for c in range(w):
        cost = grid[0][c]
        dist[0][c] = cost
        heapq.heappush(pq, (cost, 0, c))

    # Dijkstra's algorithm
    while pq:
        cost, r, c = heapq.heappop(pq)

        if cost > dist[r][c]:
            continue

        for dr in range(-1, 2):
            for dc in range(-1, 2):
                if dr == 0 and dc == 0:
                    continue

                nr, nc = r + dr, c + dc

                if 0 <= nr < h and 0 <= nc < w:
                    new_cost = cost + grid[nr][nc]
                    if new_cost < dist[nr][nc]:
                        dist[nr][nc] = new_cost
                        parent[nr][nc] = (r, c)
                        heapq.heappush(pq, (new_cost, nr, nc))

    min_final_cost = float('inf')
    end_c = -1
    for c in range(w):
        if dist[h - 1][c] < min_final_cost:
            min_final_cost = dist[h - 1][c]
            end_c = c

    output_grid = [list(map(str, row)) for row in grid]
    
    curr_r, curr_c = h - 1, end_c
    while curr_r is not None:
        output_grid[curr_r][curr_c] = ' '
        if parent[curr_r][curr_c] is None:
            break
        curr_r, curr_c = parent[curr_r][curr_c]

    for row in output_grid:
        print("".join(row))
    print()  

    return True

if __name__ == "__main__":
    while solve_block_crusher():
        pass