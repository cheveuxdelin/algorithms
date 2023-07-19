# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# WITH GLOBAL VARIABLE
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        result = root.val

        def ƒ(node) -> int:
            nonlocal result
            if not node:
                return 0

            left_max = max(ƒ(node.left), 0)
            right_max = max(ƒ(node.right), 0)

            result = max(result, node.val + left_max + right_max)

            return node.val + max(left_max, right_max)
        
        ƒ(root)
        return result