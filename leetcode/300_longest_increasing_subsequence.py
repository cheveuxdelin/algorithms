
# BRUTE FORCE
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        def h(current, previous):
            if current == len(nums):
                return 0
            c1 = 0
            if previous == -1 or nums[current] > nums[previous]:
                c1 = 1 + h(current+1, current)
            return max(c1, h(current+1, previous))
        return h(0, -1)

# TOP DOWN
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        dp = [[-1 for _ in range(len(nums))] for _ in range(len(nums))]
        def h(current, previous):
            if current == len(nums):
                return 0
            if dp[current][previous+1] == -1:
                c1 = 0
                if previous == -1 or nums[current] > nums[previous]:
                    c1 = 1 + h(current+1,current)
                dp[current][previous+1] = max(c1, h(current+1, previous))
            return dp[current][previous+1]
        return h(0, -1)

# BOTTOM UP
class Solution:
    def lengthOfLIS(self, nums: list[int]) -> int:
        dp = [1 for _ in range(len(nums))]
        rtn = 0
        for i in range(len(nums)):
            for j in range(i):
                if nums[j] < nums[i]:
                    dp[i] = max(dp[i], dp[j]+1)
            rtn = max(rtn, dp[i])
        return rtn
