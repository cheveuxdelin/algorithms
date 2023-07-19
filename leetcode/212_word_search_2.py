class Solution:
    def findWords(self, board: list[list[str]], words: list[str]) -> list[str]:
        m = len(board)
        n = len(board[0])
        axis = [0, 1, 0, -1, 0]
        words_in_grid = []

        def ƒ(current_word: str, index: int, i: int, j: int):
            if index == len(current_word):
                return True

            if i < 0 or i >= m or j < 0 or j >= n or board[i][j] == "":
                return False

            if board[i][j] == current_word[index]:
                tmp = board[i][j]
                board[i][j] = ""
                for ax in range(len(axis)-1):
                    x = i+axis[ax]
                    y = j+axis[ax+1]
                    if ƒ(current_word, index+1, x, y):
                        board[i][j] = tmp
                        return True
                board[i][j] = tmp
            return False

        for word in words:
            found_word = False
            for i in range(m):
                if found_word:
                    break
                for j in range(n):
                    if ƒ(word, 0, i, j):
                        found_word = True
                        words_in_grid.append(word)
                        break

        return words_in_grid


Solution().findWords([["a"]], ["a"])
