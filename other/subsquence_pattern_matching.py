
# BRUTE FORCE
def find_SPM_count(str, pat):
    def ƒ(index: int = 0, current: int = 0):
        if current == len(pat):
            return 1
        else:
            rtn = 0
            for i in range(index, len(str)):
                if str[i] == pat[current]:
                    rtn += ƒ(i+1, current+1)
            return rtn
    return ƒ()


# TOP DOWN
def find_SPM_count(str, pat):
    dp = [[-1 for _ in range(len(pat))] for _ in range(len(str))]

    def ƒ(index: int = 0, current: int = 0):
        if current == len(pat):
            return 1
        if dp[index][current] == -1:
            rtn = 0
            for i in range(index, len(str)):
                if str[i] == pat[current]:
                    rtn += ƒ(i+1, current+1)
            dp[index][current] = rtn
        return dp[index][current]
    return ƒ()


def main():
    print(find_SPM_count("baxmx", "ax"))
    print(find_SPM_count("tomorrow", "tor"))


main()
