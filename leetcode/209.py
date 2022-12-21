import math

class Solution:
    def minSubArrayLen(self, target: int, nums: list[int]) -> int:
        i = 0
        current = 0
        _min = math.inf
        for j in range(len(nums)):
            current += nums[j]
            while i < j and current-nums[i] >= target:
                current -= nums[i]
                i += 1
            if current >= target:
                _min = min(_min, j-i+1)
        return 0 if _min == math.inf else _min