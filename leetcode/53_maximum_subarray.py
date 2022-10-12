class Solution:
    def maxSubArray(self, nums: list[int]) -> int:
        current = 0
        _max = nums[0]
        for num in nums:
            current = max(num, current + num)
            _max = max(_max, current)
        return _max