class Solution:
    def minimumCardPickup(self, cards: List[int]) -> int:
        d = {}
        rtn = math.inf
        for i in range(len(cards)):
            if cards[i] in d:
                rtn = min(rtn, i-d[cards[i]]+1)
            d[cards[i]] = i
        return -1 if rtn == math.inf else rtn