class Solution:
    def shipWithinDays(self, weights: list[int], days: int) -> int:
        def enough(capacity: int) -> bool:
            i = 0
            for _ in range(days):
                current_capacity = capacity
                while i < len(weights) and current_capacity >= weights[i]:
                    current_capacity -= weights[i]
                    i += 1
                if i == len(weights):
                    return True
            return False
                
        left = max(weights)
        right = sum(weights)
        while left < right:
            mid = (left + right) // 2
            if enough(mid):
                right = mid
            else:
                left = mid+1
        return left
