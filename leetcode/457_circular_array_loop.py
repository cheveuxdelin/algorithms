class Solution:
    def circularArrayLoop(self, nums: list[int]) -> bool:
        def get_next_index(i: int) -> int:
            return nums[i] % len(nums)

        def get_direction(i: int) -> bool:
            return nums[i] > 0

        for i in range(len(nums)):
            