class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        minimum = prices[0]
        _max = 0

        for num in prices:
            minimum = min(minimum, num)
            _max = max(_max, num - minimum)
        return _max