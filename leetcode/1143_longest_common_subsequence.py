# TOP DOWN
class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        dp = [[-1 for _ in range(len(text2))] for _ in range(len(text1))]

        def h(i1: int, i2: int):
            if i1 == len(text1) or i2 == len(text2):
                return 0

            if dp[i1][i2] == -1:
                if text1[i1] == text2[i2]:
                    dp[i1][i2] = h(i1+1, i2+1)+1
                else:
                    dp[i1][i2] = max(
                        h(i1+1, i2),
                        h(i1, i2+1)
                    )
            return dp[i1][i2]
        return h(0, 0)


# BOTTOM UP
class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        dp = [[0 for _ in range(len(text2)+1)] for _ in range(len(text1)+1)]
        for i in range(1, len(text1)+1):
            for j in range(1, len(text2)+1):
                if text1[i-1] == text2[j-1]:
                    dp[i][j] = dp[i-1][j-1]+1
                else:
                    dp[i][j] = max(
                        dp[i-1][j],
                        dp[i][j-1]
                    )
        return dp[-1][-1]
