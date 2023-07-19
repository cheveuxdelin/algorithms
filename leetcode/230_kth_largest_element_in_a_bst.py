# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:

        def ƒ(node):
            nonlocal k
            if not node:
                return -1

            if (left := ƒ(node.left)) != -1:
                return left

            k -= 1
            if k == 0:
                return node.val
            
            return ƒ(node.right)
        return ƒ(root)