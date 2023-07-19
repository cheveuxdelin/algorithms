# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

import math


class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        last_number = -math.inf

        def ƒ(node):
            nonlocal last_number
            if not node:
                return True

            if not ƒ(node.left):
                return False

            if last_number >= node.val:
                return False
            
            last_number = node.val

            if not ƒ(node.right):
                return False
            
            return True
        return ƒ(root)