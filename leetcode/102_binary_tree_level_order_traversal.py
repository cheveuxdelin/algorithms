# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque


class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        rtn = []
        q = deque()

        if root:
            q.append(root)

        while q:
            current_level = []
            for _ in range(len(q)):
                current_node = q.popleft()
                if current_node.left:
                    q.append(current_node.left)
                if current_node.right:
                    q.append(current_node.right)
                current_level.append(current_node.val)
            rtn.append(current_level)
        return rtn