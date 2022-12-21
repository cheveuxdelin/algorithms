from collections import defaultdict
import collections
import heapq
import math


class Solution:
    def networkDelayTime(self, times: list[list[int]], n: int, k: int) -> int:
        edges = collections.defaultdict(list)
        for u, v, w in times:
            edges[u].append((w, v))
        min_heap = [(0, k)]
        visited = set()
        t = 0
        while min_heap:
            w, current = heapq.heappop(min_heap)
            if current not in visited:
                visited.add(current)
                t = max(t, w)
                for n_w, n_node in edges[current]:
                    if n_node not in visited:
                        heapq.heappush(min_heap, (n_w+w, n_node))
        return t if len(visited) == n else -1