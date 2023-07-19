# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:

        def ƒ(current_node):
            if not current_node:
                return 0

            return 1 + max(
                ƒ(current_node.left),
                ƒ(current_node.right),
            )

        return ƒ(root)

