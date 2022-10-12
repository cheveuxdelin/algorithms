class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        d = {}
        for i in range(len(nums)):
            missing_number = target - nums[i]
            if missing_number in d:
                return [d[missing_number], i]
            else:
                d[nums[i]] = i