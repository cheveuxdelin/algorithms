
# TLE
class Solution:
    def exist(self, board: list[list[str]], word: str) -> bool:
        axis = [0, 1, 0, -1, 0]
        m = len(board)
        n = len(board[0])

        def h(i: int, j: int, current_index: int) -> bool:
            if current_index == len(word):
                return True
            else:
                tmp = board[i][j]
                board[i][j] = ""
                for ax in range(len(axis)-1):
                    ii = i+axis[ax]
                    jj = j+axis[ax+1]
                    if 0 <= ii < m and 0 <= jj < n and word[current_index] == board[ii][jj] and h(ii, jj, current_index+1):
                        print(board)
                        return True
                board[i][j] = tmp
            return False

        for i in range(m):
            for j in range(n):
                if word[0] == board[i][j] and h(i, j, 1):
                    return True
        return False
