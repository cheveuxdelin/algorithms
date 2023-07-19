class Solution:
    def validPalindrome(self, s: str) -> bool:
        i = 0
        j = len(s)-1

        def ƒ(i: int, j: int) -> bool:
            while i < j:
                if s[i] != s[j]:
                    return False
                i += 1
                j -= 1
            return True

        while i < j:
            if s[i] != s[j]:
                return ƒ(i+1, j) or ƒ(i, j-1)
            i += 1
            j -= 1
        return True
