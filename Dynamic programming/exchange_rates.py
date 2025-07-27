import sys
input = sys.stdin.read

data = input().split()
i = 0
res = []

while True:
    d = int(data[i])
    i += 1
    if d == 0:
        break
    rates = list(map(float, data[i:i+d]))
    i += d
    dp = [[0.0, 0.0] for _ in range(d+1)]
    dp[0][0] = 1000.0
    for day in range(1, d+1):
        rate = rates[day-1]
        dp[day][0] = max(dp[day-1][0], int(dp[day-1][1] * rate * 0.97 * 100) / 100)
        dp[day][1] = max(dp[day-1][1], int(dp[day-1][0] / rate * 0.97 * 100) / 100)
    res.append(f"{dp[d][0]:.2f}")

print("\n".join(res))
