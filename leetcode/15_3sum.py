class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        nums.sort()
        rtn = []
        for i in range(len(nums)-2):
            if i == 0 or (nums[i] != nums[i-1]):
                a = i+1
                b = len(nums)-1
                while a < b:
                    x = nums[i]+nums[a]+nums[b]
                    if x == 0:
                        rtn.append([nums[i], nums[a], nums[b]])
                        a += 1
                        while a < b and nums[a] == nums[a-1]:
                            a += 1
                    elif x < 0:
                        a += 1
                    else:
                        b -= 1
        return rtn
