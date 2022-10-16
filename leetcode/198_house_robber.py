class Solution:
    def rob(self, nums: list[int]) -> int:
        if len(nums) <= 2:
            return max(nums)
        a = nums[0]
        b = max(nums[0], nums[1])
        for i in range(2, len(nums)):
            c = max(nums[i]+a, b)
            a = b
            b = c
        return b