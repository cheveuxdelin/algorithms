import bisect


class Solution:
    def smallestDistancePair(self, nums: list[int], k: int) -> int:
        nums.sort()
        n = len(nums)

        def enough(distance) -> bool:  # two pointers
            count, i, j = 0, 0, 0
            while i < n or j < n:
                while j < n and nums[j] - nums[i] <= distance: #fast pointer
                    j += 1
                count += j - i - 1  # count pairs
                i += 1  # move slow pointer
            return count >= k

        left = 0
        right = nums[-1] - nums[0]
        while left < right:
            mid = (left + right) // 2
            if enough(mid):
                right = mid
            else:
                left = mid + 1


Solution().smallestDistancePair([1, 3, 1], 1)
