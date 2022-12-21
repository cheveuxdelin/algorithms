
# BRUTE FORCE
def find_LPS_length(s: str) -> str:

    def ƒ(i: int = 0, j: int = len(s)-1) -> int:
        if i == j:
            return 1
        if i > j:
            return 0
        if s[i] == s[j] and j-i-1 == ƒ(i+1, j-1):
            return j-i+1
        else:
            return max(
                ƒ(i, j-1),
                ƒ(i+1, j)
            )
    return ƒ()


# TOP DOWN
def find_LPS_length(s: str) -> str:
    dp = [[-1 for _ in range(len(s))] for _ in range(len(s))]

    def ƒ(i: int = 0, j: int = len(s)-1) -> int:
        if i == j:
            return 1
        if i > j:
            return 0
        if dp[i][j] == -1:
            if s[i] == s[j] and j-i-1 == ƒ(i+1, j-1):
                dp[i][j] = j-i+1
            else:
                dp[i][j] = max(
                    ƒ(i, j-1),
                    ƒ(i+1, j)
                )
        return dp[i][j]
    return ƒ()


# BOTTOM UP
def find_LPS_length(s: str) -> str:
    dp = [[False for _ in range(len(s))] for _ in range(len(s))]
    _max = 1
    for i in range(len(s)):
        dp[i][i] = True

    for i in range(len(s)-1, -1, -1):
        for j in range(i+1, len(s)):
            if s[i] == s[j] and (dp[i+1][j-1] or j-i == 1):
                dp[i][j] = True
                _max = max(_max, j-i+1)
    return _max




def main():
    print(find_LPS_length("abdbca"))
    print(find_LPS_length("cddpd"))
    print(find_LPS_length("pqr"))


main()
