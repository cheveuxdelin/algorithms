class Solution:
    def splitArray(self, nums: list[int], k: int) -> int:
        def enough(s: int) -> bool:
            i = 0
            for _ in range(k):
                current_s = s
                while i < len(nums) and current_s >= nums[i] :
                    current_s -= nums[i]
                    i += 1
                if i == len(nums):
                    return True
            return False

        left = max(nums)
        right = sum(nums)
        while left < right:
            mid = (left + right) // 2
            if enough(mid):
                right = mid
            else:
                left = mid + 1
        return left
