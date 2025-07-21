def matches(p, f):
    m, n = len(p), len(f)
    dp = [[False] * (n + 1) for _ in range(m + 1)]
    dp[0][0] = True

    for i in range(1, m + 1):
        if p[i - 1] == '*':
            dp[i][0] = dp[i - 1][0]

    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if p[i - 1] == '*':
                dp[i][j] = dp[i - 1][j] or dp[i][j - 1]
            elif p[i - 1] == f[j - 1]:
                dp[i][j] = dp[i - 1][j - 1]

    return dp[m][n]

P = input()
N = int(input())
files = [input() for _ in range(N)]

for f in files:
    if matches(P, f):
        print(f)
