# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.

        :type root: TreeNode
        :rtype: str
        """
        return f"{root.val},{self.serialize(root.left)},{self.serialize(root.right)}" if root else "null"

    def deserialize(self, data: str):
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """
        index = 0
        values = data.split(",")

        def ƒ():
            nonlocal index
            if values[index] == "null":
                index += 1
                return None
            else:
                new_node = TreeNode(int(values[index]))
                index += 1
                new_node.left = ƒ()
                new_node.right = ƒ()
                return new_node
        return ƒ()

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))
