class Solution:
    def minDays(self, bloomDay: list[int], m: int, k: int) -> int:
        n = len(bloomDay)
        if m*k > n:
            return -1

        def feasible(day: int) -> bool:
            count = 0
            current = 0
            for i in range(n):
                current = current+1 if bloomDay[i] <= day else 0
                if current == k:
                    current = 0
                    count += 1
                    if count == m:
                        break
            return count == m

        left = min(bloomDay)
        right = max(bloomDay)
        while left < right:
            mid = (left + right) // 2
            if feasible(mid):
                right = mid
            else:
                left = mid+1
        return left