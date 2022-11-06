from collections import deque


class Solution:
    def findBall(self, grid: list[list[int]]) -> list[int]:
        m = len(grid)
        n = len(grid[0])
        q = deque()
        unvisited = -2
        visited = [[unvisited for _ in range(n)] for _ in range(m)]
        final_positions = [-1 for _ in range(n)]
        for current_ball in range(n):
            col = current_ball
            for row in range(m):
                if visited[row][col] == unvisited:
                    q.append((row, col))
                    next_col = col+grid[row][col]
                    if next_col == -1 or next_col == n or grid[row][col] != grid[row][next_col]:
                        col = -1
                        break
                    else:
                        col = next_col
                else:
                    col = visited[row][col]
                    break
            while q:
                c_row, c_col = q.pop()
                visited[c_row][c_col] = col
            final_positions[current_ball] = col
        return final_positions
