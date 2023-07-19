
class Solution:
    def smallestDistancePair(self, nums: list[int], k: int) -> int:
        nums.sort()
        n = len(nums)

        def enough(distance: int) -> bool:
            count = 0
            i = 0
            j = 0
            while i < n:
                while j < n and nums[j] - nums[i] <= distance:
                    j += 1
                count += j-i-1
                i += 1
            return count >= k

        left = 0
        right = nums[-1] - nums[0]

        while left < right:
            mid = (left + right) // 2
            if enough(mid):
                right = mid
            else:
                left = mid + 1

        return left


Solution().smallestDistancePair([0,1,2,3,4,5,6,7,8,9], 3)
