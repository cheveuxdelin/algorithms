# BACKTRACKING
class Solution:
    def generateParenthesis(self, n: int) -> list[str]:
        rtn = []

        def ƒ(current: str="", open=0, close=0):
            if len(current) == n * 2:
                rtn.append(current)
            else:
                if open < n:
                    ƒ(current+"(", open+1, close)
                if close < open:
                    ƒ(current+")", open, close+1)
        ƒ()
        return rtn
