import sys
import bisect

input = sys.stdin.read
data = input().split()

N = int(data[0])
H = int(data[1])
obstacles = list(map(int, data[2:]))

bottom = []
top = []

for i in range(N):
    if i % 2 == 0:
        bottom.append(obstacles[i])
    else:
        top.append(obstacles[i])

bottom.sort()
top.sort()

min_obstacles = N
count = 0

for height in range(1, H + 1):
    b = len(bottom) - bisect.bisect_left(bottom, height)
    t = len(top) - bisect.bisect_left(top, H - height + 1)
    total = b + t

    if total < min_obstacles:
        min_obstacles = total
        count = 1
    elif total == min_obstacles:
        count += 1

print(f"{min_obstacles} {count}")
