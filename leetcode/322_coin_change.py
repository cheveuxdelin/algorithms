import math

class Solution:
    def coinChange(self, coins: list[int], amount: int) -> int:
        dp = [math.inf for _ in range(amount+1)]
        dp[0] = 0
        for i in range(len(dp)):
            for coin in coins:
                if i - coin >= 0:
                    dp[i] = min(dp[i], dp[i-coin]+1)
        return dp[-1] if dp[-1] != math.inf else -1
    