import time
import matplotlib.pyplot as plt
import random

def knapsack(weights, profits, capacity):
    n = len(weights)
    dp = [[0 for _ in range(capacity + 1)] for _ in range(n + 1)]

    for i in range(1, n + 1):
        for w in range(capacity + 1):
            if weights[i - 1] <= w:
                dp[i][w] = max(
                    profits[i - 1] + dp[i - 1][w - weights[i - 1]],
                    dp[i - 1][w]
                )
            else:
                dp[i][w] = dp[i - 1][w]
    return dp[n][capacity]

# Store input sizes and corresponding times
input_sizes = list(range(10, 210, 20))  # From 10 to 200 items
times = []

for n in input_sizes:
    weights = [random.randint(1, 50) for _ in range(n)]
    profits = [random.randint(1, 100) for _ in range(n)]
    capacity = random.randint(50, 150)

    start = time.time()
    knapsack(weights, profits, capacity)
    end = time.time()
    
    times.append(end - start)

# Plotting
plt.figure(figsize=(10, 6))
plt.plot(input_sizes, times, marker='o', color='purple')
plt.title('0/1 Knapsack: Input Size vs Running Time')
plt.xlabel('Number of Items')
plt.ylabel('Execution Time (seconds)')
plt.grid(True)
plt.tight_layout()
plt.show()
