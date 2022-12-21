# BOTTOM UP (TLE)
class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        _max = [0, 0]
        dp = [[False for _ in range(n)] for _ in range(n)]
        for i in range(n):
            dp[i][i] = 1
        for i in range(n-1, -1, -1):
            for j in range(i+1, n):
                if s[i] == s[j] and (dp[i+1][j-1] or j-i == 1):
                    dp[i][j] = True
                    _max = max(_max, [i, j], key=lambda x: x[1]-x[0])
        return s[_max[0]:_max[1]+1]

# GROWING FROM MIDDLE


class Solution:
    def longestPalindrome(self, s: str) -> str:
        def ƒ(i: int, j: int):
            while i >= 0 and j < len(s) and s[i] == s[j]:
                i -= 1
                j += 1
            return j-i-1
        start = 0
        end = 0
        for i in range(len(s)):
            if (x := max(ƒ(i, i), ƒ(i, i+1))) > end - start:
                start = i - (x - 1) // 2
                end = i + x // 2
        return s[start:end+1]
