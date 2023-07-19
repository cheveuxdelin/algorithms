import math


class Solution:
    def minEatingSpeed(self, piles: list[int], h: int) -> int:
        def feasible(speed: int):
            return sum(math.ceil(pile / speed) for pile in piles) <= h

        left = 1
        right = max(piles)
        while left < right:
            mid = (left + right) // 2
            if feasible(mid):
                right = mid
            else:
                left = mid+1
        return left