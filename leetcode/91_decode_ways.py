# TOP DOWN
class Solution:
    def numDecodings(self, s: str) -> int:
        dp = [0 for _ in range(len(s)+1)]
        dp[len(s)] = 1

        def dfs(i):
            if dp[i] != 0:
                return dp[i]
            if s[i] == "0":
                return 0
            dp[i] = dfs(i+1)
            if i != len(s)-1 and (s[i] == "1" or (s[i] == "2" and 0 <= int(s[i+1]) <= 6)):
                dp[i] += dfs(i+2)
            return dp[i]
        return dfs(0)


# BOTTOM UP
class Solution:
    def numDecodings(self, s: str) -> int:
        dp = {len(s): 1}
        for i in range(len(s)-1, -1, -1):
            if s[i] == "0":
                dp[i] = 0
            else:
                dp[i] = dp[i+1]

            if (i+1 < len(s)) and (s[i] == "1" or s[i] == "2" and s[i+1] in "0123456"):
                dp[i] += dp[i+2]
        return dp[0]
