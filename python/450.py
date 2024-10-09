# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        def delete(node):
            if not node.left and not node.right:
                return
            if not node.left:
                return node.right
            if not node.right:
                return node.left
            left = node.left
            right = node.right
            node1 = right
            while node1.left:
                node1 = node1.left
            node1.left = left
            return right
        if not root:
            return
        if root.val == key:
            return delete(root)
        root.left = self.deleteNode(root.left, key)
        root.right = self.deleteNode(root.right, key)
        return root
