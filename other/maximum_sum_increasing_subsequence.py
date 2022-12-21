
def find_MSIS(nums: int):
    rtn = 0
    dp = [nums[i] for i in range(len(nums))]
    for i in range(len(nums)):
        for j in range(i):
            if dp[j] < dp[i]:
                dp[i] = max(dp[i], nums[i] + dp[j])
        rtn = max(rtn, dp[i])
    return rtn


def main():
    print(find_MSIS([4, 1, 2, 6, 10, 1, 12]))
    print(find_MSIS([-4, 10, 3, 7, 15]))


main()
