# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        def ƒ(c1, c2) -> bool:
            if not c1 and not c2:
                return True

            if (c1 and not c2) or (c2 and not c1):
                return False

            return c1.val == c2.val and ƒ(c1.left, c2.left) and ƒ(c1.right, c2.right)
        
        return ƒ(p, q)