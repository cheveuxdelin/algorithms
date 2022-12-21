# BRUTE FORCE
def find_SCS_length(s1, s2):
    def ƒ(i: int, j: int) -> int:
        if i == len(s1):
            return len(s2) - j
        if j == len(s2):
            return len(s1) - i

        if s1[i] == s2[j]:
            return 1 + ƒ(i + 1, j + 1)
        else:
            return min(
                1 + ƒ(i + 1, j),
                1 + ƒ(i, j + 1),
            )

    return ƒ(0, 0)


# TOP DOWN
def find_SCS_length(s1, s2):
    dp = [[-1 for _ in range(len(s2))] for _ in range(len(s1))]

    def ƒ(i: int = 0, j: int = 0) -> int:
        if i == len(s1):
            return len(s2) - j
        if j == len(s2):
            return len(s1) - i
        if dp[i][j] == -1:
            if s1[i] == s2[j]:
                dp[i][j] = 1 + ƒ(i + 1, j + 1)
            else:
                dp[i][j] = min(
                    1 + ƒ(i + 1, j),
                    1 + ƒ(i, j + 1),
                )
        return dp[i][j]

    return ƒ()

# BOTTOM UP
def find_SCS_length(s1, s2):
    dp = [[0 for _ in range(len(s2)+1)] for _ in range(len(s1)+1)]
    for i in range(len(s1)+1):
        dp[i][0] = i
    for i in range(len(s2)+1):
        dp[0][i] = i

    for i in range(1,len(s1)+1):
        for j in range(1,len(s2)+1):
            if s1[i] == s2[j]:
                dp[i][j] = 1 + dp[i-1][j-1]
            else:
                dp[i][j] = 1 + min(dp[i][j-1], dp[i-1][j])
    return dp[-1][-1]

def main():
    print(find_SCS_length("abcf", "bdcf"))
    print(find_SCS_length("dynamic", "programming"))


main()
