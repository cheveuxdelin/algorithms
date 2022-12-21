import heapq


class Solution:
    def lastStoneWeight(self, stones: list[int]) -> int:
        h = heapq._heapify_max(stones)
        heapq._heappop_max()
