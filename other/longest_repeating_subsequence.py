# BRUTE FORCE
def find_LRS_length(str: str):
    def ƒ(i1, i2):
        if i1 == len(str) or i2 == len(str):
            return 0
        if i1 != i2 and str[i1] == str[i2]:
            return 1 + ƒ(i1+1, i2+1)
        return max(
            ƒ(i1, i2+1),
            ƒ(i1+1, i2),
        )
    return ƒ(0, 0)


# TOP DOWN
def find_LRS_length(str: str):
    dp = [[-1 for _ in range(len(str))] for _ in range(len(str))]

    def ƒ(i1, i2):
        if i1 == len(str) or i2 == len(str):
            return 0
        if dp[i1][i2] == -1:
            if i1 != i2 and str[i1] == str[i2]:
                dp[i1][i2] = 1 + ƒ(i1+1, i2+1)
            else:
                dp[i1][i2] = max(
                    ƒ(i1, i2+1),
                    ƒ(i1+1, i2),
                )
        return dp[i1][i2]
    return ƒ(0, 0)


# BOTTOM UP
def find_LRS_length(str: str):
    dp = [[0 for _ in range(len(str)+1)] for _ in range(len(str)+1)]
    _max = 0
    for i in range(1, len(str)+1):
        for j in range(1, len(str)+1):
            if i != j and str[i-1] == str[j-1]:
                dp[i][j] = 1 + dp[i-1][j-1]
            else:
                dp[i][j] = max(dp[i-1][j], dp[i][j-1])
        _max = max(_max, dp[i][j])
    return _max


def main():
    print(find_LRS_length("tomorrow"))
    print(find_LRS_length("aabdbcec"))
    print(find_LRS_length("fmff"))


main()
