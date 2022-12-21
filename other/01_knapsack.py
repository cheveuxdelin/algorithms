
# BRUTE FOCE
def solve_knapsack(profits, weights, capacity):
    def ƒ(index: int = 0, cap: int = capacity):
        if index == len(profits) or cap <= 0:
            return 0
        else:
            return max(
                ƒ(index+1, cap),
                profits[index] + ƒ(index+1, cap-weights[index]) if weights[index] <= cap else 0
            )
    return ƒ()

# TOP DOWN


def solve_knapsack(profits, weights, capacity):
    dp = [[-1 for _ in range(capacity+1)] for _ in range(len(profits))]

    def ƒ(index: int = 0, cap: int = capacity):
        if index == len(profits) or cap <= 0:
            return 0
        if dp[index][cap] == -1:
            dp[index][cap] = max(
                ƒ(index+1, cap),
                profits[index] + ƒ(index+1, cap-weights[index]) if weights[index] <= cap else 0
            )
        return dp[index][capacity]
    return ƒ()


def solve_knapsack(profits, weights, capacity):
    dp = [[0 for _ in range(capacity+1)] for _ in range(len(profits))]

    for c in range(capacity+1):
        if weights[0] <= capacity:
            dp[0][c] = profits[0]

    for i in range(1, len(profits)):
        for j in range(1, capacity+1):
            dp[i][j] = max(
                dp[i-1][j],
                profits[i] + dp[i-1][j - weights[i]] if weights[i] <= j else 0
            )
    return dp[-1][-1]


def main():
    print(solve_knapsack([1, 6, 10, 16], [1, 2, 3, 5], 7))
    print(solve_knapsack([1, 6, 10, 16], [1, 2, 3, 5], 6))


main()
