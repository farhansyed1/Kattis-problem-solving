import sys

def knapsack(capacity, weights, values):
    n = len(weights)
    dp = [[0] * (capacity + 1) for _ in range(n + 1)]
    
    for i in range(1, n + 1):
        for w in range(capacity + 1):
            if weights[i - 1] <= w:
                dp[i][w] = max(dp[i - 1][w],
                               dp[i - 1][w - weights[i - 1]] + values[i - 1])
            else:
                dp[i][w] = dp[i - 1][w]

    res = dp[n][capacity]
    w = capacity
    selected_indices = []
    
    for i in range(n, 0, -1):
        if res <= 0:
            break
        if res != dp[i - 1][w]:
            selected_indices.append(i - 1)
            res -= values[i - 1]
            w -= weights[i - 1]
    
    return selected_indices

def process_input():
    input_lines = sys.stdin.read().strip().split('\n')
    idx = 0
    results = []
    
    while idx < len(input_lines):
        if input_lines[idx].strip() == '':
            idx += 1
            continue

        C, n = map(int, input_lines[idx].split())
        idx += 1

        values = []
        weights = []

        for _ in range(n):
            v, w = map(int, input_lines[idx].split())
            values.append(v)
            weights.append(w)
            idx += 1

        selected = knapsack(C, weights, values)
        results.append(f"{len(selected)}\n{' '.join(map(str, selected))}")
    
    print('\n'.join(results))

if __name__ == "__main__":
    process_input()
