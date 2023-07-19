class Solution:
    def findKthNumber(self, m: int, n: int, k: int) -> int:
        def enough(num: int) -> bool:
            total = 0
            for row in range(1, m+1):
                current = min(n, num // row)
                if current == 0:
                    break
                total += current
            return total >= k
                

        left = 1
        right = m*n
        while left < right:
            mid = (left + right) // 2
            if enough(mid):
                right = mid
            else:
                left = mid + 1
        return left