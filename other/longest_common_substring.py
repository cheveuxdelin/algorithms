
def longest_common_substring_recursive(s1: str, s2: str) -> int:

    def ƒ(i1: int = 0, i2: int = 0) -> int:
        if i1 == len(s1) or i2 == len(s2):
            return 0

        if s1[i1] == s2[i2]:
            return 1 + ƒ(i1+1, i2+1)
        else:
            return max(
                ƒ(i1, i2+1),
                ƒ(i1+1, i2)
            )
    return ƒ()


def longest_common_substring_top_down(s1: str, s2: str) -> int:

    dp = [[-1 for _ in range(len(s2))] for _ in range(len(s1))]

    def ƒ(i1: int = 0, i2: int = 0) -> int:
        if i1 == len(s1) or i2 == len(s2):
            return 0

        if dp[i1][i2] == -1:
            if s1[i1] == s2[i2]:
                dp[i1][i2] = 1 + ƒ(i1+1, i2+1)
            else:
                dp[i1][i2] = max(
                    ƒ(i1, i2+1),
                    ƒ(i1+1, i2)
                )
        return dp[i1][i2]
    return ƒ()


def longest_common_substring_bottom_up(s1: str, s2: str) -> int:
    dp = [[0 for _ in range(len(s2)+1)] for _ in range(len(s1)+1)]
    max_length = 0
    for i1 in range(1, len(s1)+1):
        for i2 in range(1, len(s2)+1):
            if s1[i1-1] == s2[i2-1]:
                dp[i1][i2] = 1 + dp[i1-1][i2-1]
                max_length = max(max_length, dp[i1][i2])
    return max_length


def longest_common_substring_bottom_up_space_optimized(s1: str, s2: str) -> int:
    dp = [0 for _ in range(len(s2)+1)]
    max_length = 0
    for i1 in range(1, len(s1)+1):
        for i2 in range(len(s2), 0, -1):
            print(dp)
            if s1[i1-1] == s2[i2-1]:
                dp[i2] = 1 + dp[i2-1]
            else:
                dp[i2] = 0
            max_length = max(max_length, dp[i2])
    return max_length


x = longest_common_substring_bottom_up_space_optimized("abasdfasldcñjaweñfkajwea", "sldcñjawe")
print(x)
