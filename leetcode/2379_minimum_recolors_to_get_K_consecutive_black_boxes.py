import math


class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        i = 0
        n_black_boxes = 0
        min_boxes_needed = math.inf
        for j in range(len(blocks)):
            if blocks[j] == "B":
                n_black_boxes += 1
            if j >= k:
                if blocks[i] == "B":
                    n_black_boxes -= 1
                i += 1
            min_boxes_needed = min(min_boxes_needed, k - n_black_boxes)
        return min_boxes_needed
