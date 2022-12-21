class Solution:
    def splitArray(self, nums: list[int], k: int) -> int:
        def possible(subarray_sum: int) -> bool:
            i = 0
            for _ in range(k):
                current_sum = subarray_sum
                while i < len(nums) and current_sum >= nums[i]:
                    current_sum -= nums[i]
                    i += 1
                if i == len(nums):
                    return True
            return False

        left = max(nums)
        right = sum(nums)
        while left < right:
            mid = (left + right) // 2
            if possible(mid):
                right = mid
            else:
                left = mid+1
        return left
