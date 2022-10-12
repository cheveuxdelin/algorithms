class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        left_to_right = [1 for _ in range(len(nums))]
        right_to_left = [1 for _ in range(len(nums))]

        for i in range(len(nums)-1):
            left_to_right[i+1] = left_to_right[i] * nums[i]
            right_to_left[-i-2] = right_to_left[-i-1] * nums[-i-1]

        return [left_to_right[i] * right_to_left[i] for i in range(len(nums))]