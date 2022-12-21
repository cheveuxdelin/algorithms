
# TOP DOWN
def find_LPS_length(st) -> int:
    dp = [[-1 for _ in range(len(st))] for _ in range(len(st))]

    def ƒ(i: int = 0, j: int = len(st)-1):
        if i == j:
            return 1
        elif i > j:
            return 0

        if dp[i][j] == -1:
            if st[i] == st[j]:
                dp[i][j] = 2 + ƒ(i+1, j-1)
            else:
                dp[i][j] = max(
                    ƒ(i, j-1),
                    ƒ(i+1, j)
                )
        return dp[i][j]

    return ƒ()


def find_LPS_length(st):
    n = len(st)
    # dp[i][j] stores the length of LPS from index 'i' to index 'j'
    dp = [[0 for _ in range(n)] for _ in range(n)]

    # every sequence with one element is a palindrome of length 1
    for i in range(n):
        dp[i][i] = 1

    for startIndex in range(n - 1, -1, -1):
        for endIndex in range(startIndex + 1, n):
            # case 1: elements at the beginning and the end are the same
            if st[startIndex] == st[endIndex]:
                dp[startIndex][endIndex] = 2 + dp[startIndex + 1][endIndex - 1]
            else:  # case 2: skip one element either from the beginning or the end
                dp[startIndex][endIndex] = max(
                    dp[startIndex + 1][endIndex], dp[startIndex][endIndex - 1])
    return dp[0][n - 1]


def main():
    print(find_LPS_length("abdbca"))
    print(find_LPS_length("cddpd"))
    print(find_LPS_length("pqr"))


main()
