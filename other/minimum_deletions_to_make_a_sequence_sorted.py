# BRUTE FORCE
def find_minimum_deletions(nums: list[int]):
    def ƒ(current: int = 0, previous: int = -1):
        if current == len(nums):
            return 0
        c1 = 0
        if previous == -1 or nums[previous] <= nums[current]:
            c1 = 1 + ƒ(current+1, current)
        c2 = ƒ(current+1, previous)
        return max(c1, c2)
    return len(nums) - ƒ()


# TOP DOWN
def find_minimum_deletions(nums: list[int]):
    dp = [[-1 for _ in range(len(nums))] for _ in range(len(nums))]

    def h(current, previous):
        if current == len(nums):
            return 0
        if dp[current][previous+1] == -1:
            c1 = 0
            if previous == -1 or nums[current] > nums[previous]:
                c1 = 1 + h(current+1, current)
            dp[current][previous+1] = max(c1, h(current+1, previous))
        return dp[current][previous+1]
    return len(nums) - h(0, -1)


# BOTTOM UP
def find_minimum_deletions(nums: list[int]):
    dp = [1 for _ in range(len(nums))]
    lcs_length = 0
    for i in range(len(nums)):
        for j in range(i):
            if nums[i] >= nums[j]:
                dp[i] = max(dp[i], 1+dp[j])
        lcs_length = max(lcs_length, dp[i])
    return len(nums) - lcs_length


def main():
    print(find_minimum_deletions([4, 2, 3, 6, 10, 1, 12]))
    print(find_minimum_deletions([-4, 10, 3, 7, 15]))
    print(find_minimum_deletions([3, 2, 1, 0]))


main()