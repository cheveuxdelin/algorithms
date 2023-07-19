# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        def same_tree(n1, n2) -> bool:
            if not n1 and not n2:
                return True
            if (n1 and not n2) or (n2 and not n1):
                return False
            if n1.val == n2.val and same_tree(n1.left, n2.left) and same_tree(n1.right, n2.right):
                return True
            return False

        def ƒ(node) -> bool:
            if node:
                if same_tree(node, subRoot) or ƒ(node.left) or ƒ(node.right):
                    return True
            return False

        return ƒ(root)
