from collections import deque

w, h = map(int, input().split())
grid = [list(input()) for _ in range(h)]

# Up, down, left, right
dirs = [(-1,0), (1,0), (0,-1), (0,1)]

# Find player start
for y in range(h):
    for x in range(w):
        if grid[y][x] == 'P':
            start = (y, x)

def is_safe(y, x):
    # Not a wall or trap
    if grid[y][x] == '#' or grid[y][x] == 'T':
        return False
    # If next to a trap, can't move further from here
    for dy, dx in dirs:
        ny, nx = y + dy, x + dx
        if 0 <= ny < h and 0 <= nx < w:
            if grid[ny][nx] == 'T':
                return False
    return True

visited = [[False]*w for _ in range(h)]
q = deque()
q.append(start)
visited[start[0]][start[1]] = True
gold = 0

while q:
    y, x = q.popleft()
    if grid[y][x] == 'G':
        gold += 1
    # If next to trap, don't move further from here
    danger = False
    for dy, dx in dirs:
        ny, nx = y + dy, x + dx
        if 0 <= ny < h and 0 <= nx < w:
            if grid[ny][nx] == 'T':
                danger = True
    if danger:
        continue
    for dy, dx in dirs:
        ny, nx = y + dy, x + dx
        if 0 <= ny < h and 0 <= nx < w:
            if not visited[ny][nx] and grid[ny][nx] != '#' and grid[ny][nx] != 'T':
                visited[ny][nx] = True
                q.append((ny, nx))

print(gold)