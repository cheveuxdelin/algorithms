class Solution:
    def longestConsecutive(self, nums: list[int]) -> int:
        s = set(nums)
        rtn = 0
        for num in nums:
            if num-1 not in s:
                length = 0
                while num+length in s:
                    length += 1
                rtn = max(rtn, length)
        return rtn