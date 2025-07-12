def knapsack(weights, values, capacity):
    n = len(weights)
    dp = [[0] * (capacity + 1) for _ in range(n + 1)]
    
    for i in range(1, n+1):
        for w in range(capacity + 1):
            if weights[i-1] <= w:
                dp[i][w] = max(dp[i-1][w], dp[i-1][w - weights[i-1]] + values[i-1])
            else:
                dp[i][w] = dp[i-1][w]
    return dp[n][capacity]

weights = list(map(int, input("Enter item weights: ").split()))
values = list(map(int, input("Enter item values: ").split()))
capacity = int(input("Enter max capacity: "))
print("Max value in knapsack:", knapsack(weights, values, capacity))