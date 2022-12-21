import math
import heapq


class Solution:
    def minCostConnectPoints(self, points: list[list[int]]) -> int:
        def get_distance(a, b) -> int:
            return abs(points[a][0]-points[b][0])+abs(points[a][1]-points[b][1])

        n = len(points)
        unvisited = set(range(n))
        q = [(0, 0)]
        rtn = 0
        while unvisited:
            while q[0][1] not in unvisited:
                heapq.heappop(q)
            current_cost, current_node = heapq.heappop(q)
            unvisited.discard(current_node)
            rtn += current_cost
            for i in unvisited:
                heapq.heappush(q, (get_distance(i, current_node), i))
        return rtn


Solution().minCostConnectPoints([[0, 0], [2, 2], [3, 10], [5, 2], [7, 0]])
