# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        def ƒ(current_node):
            if p.val > current_node.val < q.val:
                return ƒ(current_node.right)
            elif p.val < current_node.val > q.val:
                return ƒ(current_node.left)
            else:
                return current_node
        return ƒ(root)
