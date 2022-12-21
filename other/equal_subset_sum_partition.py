# BRUTE FORCE
def can_partition(num: list[int]):
    target = sum(num)
    if target % 2 != 0:
        return False
    target //= 2

    def ƒ(i: int = 0, p: int = 0):
        if i == len(num):
            return p == target
        else:
            return ƒ(i+1, p) or (p+num[i] <= target and ƒ(i+1, p+num[i]))
    return ƒ()


# TOP DOWN
def can_partition(num: list[int]):
    target = sum(num)
    if target % 2 != 0:
        return False
    target //= 2

    dp = [[-1 for _ in range(target+1)] for _ in range(len(num))]

    def ƒ(i: int = 0, p: int = 0) -> bool:
        if i == len(num):
            return p == target
        if dp[i][p] == -1:
            dp[i][p] = ƒ(i+1, p) or (p+num[i] <= target and ƒ(i+1, p+num[i]))
        return dp[i][p]
    return ƒ()


# BOTTOM UP
def can_partition(num: list[int]):
    target = sum(num)
    if target % 2 != 0:
        return False
    target //= 2

    dp = [[False for _ in range(target+1)] for _ in range(len(num))]

    for i in range(len(num)):
        dp[i][0] = True
    for i in range(target+1):
        dp[0][i] = i == num[0]

    for i in range(1, len(num)):
        for c in range(1, target+1):
            dp[i][c] = dp[i-1][c] or (c >= num[i] and dp[i-1][c-num[i]])
    return dp[-1][-1]


def main():
    print("Can partition: " + str(can_partition([1, 2, 3, 4])))
    print("Can partition: " + str(can_partition([1, 1, 3, 4, 7])))
    print("Can partition: " + str(can_partition([2, 3, 4, 6])))


main()
