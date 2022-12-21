def find_minimum_deletions(st):
    def lps():
        dp = [[0 for _ in range(len(st))] for _ in range(len(st))]
        for i in range(len(st)-1, -1, -1):
            dp[i][i] = 1
            for j in range(i+1, len(st)):
                dp[i][j] = 2 + dp[i+1][j-1] if st[i] == st[j] else max(dp[i][j-1], dp[i+1][j])
        return dp[0][len(st)-1]
    return len(st) - lps()


def main():
    print(find_minimum_deletions("abdbca"))
    print(find_minimum_deletions("cddpd"))
    print(find_minimum_deletions("pqr"))


main()
