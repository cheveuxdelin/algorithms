class Solution:
    def smallestDivisor(self, nums: list[int], threshold: int) -> int:
        def possible(divisor: int) -> bool:
            return sum(math.ceil(num / divisor) for num in nums) <= threshold
        left = 1
        right = max(nums)
        while left < right:
            mid = (left + right) // 2
            if possible(mid):
                right = mid
            else:
                left = mid+1
        return left