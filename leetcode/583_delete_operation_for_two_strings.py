class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        def longest_common_subsequence(w1: str, w2: str) -> int:
            dp = [[0 for _ in range(len(w2)+1)] for _ in range(len(w1)+1)]
            for i in range(1, len(w1)+1):
                for j in range(1, len(w2)+1):
                    if w1[i-1] == w2[j-1]:
                        dp[i][j] = 1 + dp[i-1][j-1]
                    else:
                        dp[i][j] = max(
                            dp[i][j-1],
                            dp[i-1][j],
                        )
            return dp[-1][-1]
        lcs_length = longest_common_subsequence(word1, word2)
        return len(word1) + len(word2) - lcs_length * 2
