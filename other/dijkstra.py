import heapq
import math


def dijkstra(graph: list[list[tuple[int, int]]], starting_node: int) -> list:
    n = len(graph)
    distances = [math.inf] * n
    distances[starting_node] = 0
    h = [(0, starting_node)]
    while h:
        current_distance, current_node = heapq.heappop(h)
        for neighbor_distance, neighbor_node in graph[current_node]:
            if (new_distance := current_distance + neighbor_distance) < distances[neighbor_node]:
                heapq.heappush(h, (new_distance, neighbor_node))
                distances[neighbor_node] = new_distance
    return distances


dijkstra(
    [
        [(4, 1), (1, 2)],
        [],
        [(1, 3)],
        [(1, 1)],
    ],
    0
)
