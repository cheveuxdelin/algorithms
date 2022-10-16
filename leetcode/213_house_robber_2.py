class Solution:
    def rob(self, nums: list[int]) -> int:
        def calculate_amount(start: int, end: int) -> int:
            a = 0
            b = 0
            for i in range(start, end):
                c = max(a+nums[i], b)
                a = b
                b = c
            return b
        if len(nums) <= 2:
            return max(nums)
        return max(
            calculate_amount(0, len(nums)-1),
            calculate_amount(1, len(nums))
        )
