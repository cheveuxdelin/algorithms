class Solution:
    def numIslands(self, grid: list[list[str]]) -> int:
        number_of_islands = 0
        axis = [0, 1, 0, -1, 0]

        def expand(i: int, j: int):
            grid[i][j] = "0"
            for ax in range(len(axis)-1):
                x = i + axis[ax]
                y = j + axis[ax+1]
                if 0 <= x < len(grid) and 0 <= y < len(grid[0]) and grid[x][y] == "1":
                    expand(x, y)

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == "1":
                    number_of_islands += 1
                    expand(i, j)
        return number_of_islands