class Solution:
    def compress(self, chars: list[str]) -> int:
        index = 0
        i = 0
        while i < len(chars):
            j = i
            while j < len(chars) and chars[i] == chars[j]:
                j += 1
            chars[index] = chars[i]
            index += 1
            if j-i > 1:
                for c in str(j-i):
                    chars[index] = c
                    index += 1
            i = j
        return index


Solution().compress(
    [
        "a", "b", "b", "b", "b",
        "b", "b", "b", "b", "b", "b", "b",
        "b",
    ]
)
