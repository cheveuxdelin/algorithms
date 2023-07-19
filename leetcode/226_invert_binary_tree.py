# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        def ƒ(current):
            if current:
                current.left, current.right = current.right, current.left
                ƒ(current.left)
                ƒ(current.right)
        ƒ(root)
        return root
