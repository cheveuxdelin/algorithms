class Solution:
    def maxProduct(self, nums: list[int]) -> int:
        rtn = max(nums)
        current_min = current_max = 1
        for n in nums:
            tmp = current_max * n
            current_max = max(n * current_max, n * current_min, n)
            current_min = min(tmp, n * current_min, n)
            rtn = max(rtn, current_max)
        return rtn
    