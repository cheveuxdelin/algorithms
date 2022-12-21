import heapq
import math


class Solution:
    def maxProbability(self, n: int, edges: list[list[int]], succProb: list[float], start: int, end: int) -> float:
        adjacency_list = [[] for _ in range(n)]
        for (v1, v2), weight in zip(edges, succProb):
            adjacency_list[v1].append((weight, v2))
            adjacency_list[v2].append((weight, v1))

        q = [(-1, start)]
        visited = [False] * n
        visited[start] = True
        while q:
            current_probability, current_node = heapq.heappop(q)
            if current_node == end:
                return -current_probability
            visited[current_node] = True
            for neighbor_probability, neighbor_node in adjacency_list[current_node]:
                if not visited[neighbor_node]:
                    heapq.heappush(q, (current_probability*neighbor_probability, neighbor_node))
        return 0


Solution().maxProbability(n=3, edges=[[0, 1], [1, 2], [0, 2]], succProb=[0.5, 0.5, 0.2], start=0, end=2)
