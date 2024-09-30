# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def height(node):
            if not node:
                return 0
            left = height(node.left)
            right = height(node.right)
            if left == -1 or right == -1:
                return -1
            if abs(left - right) > 1:
                return -1
            return max(left, right) + 1
        if not root:
            return True
        left = height(root.left)
        if left == -1:
            return False
        right = height(root.right)
        if right == -1:
            return False
        if abs(left - right) > 1:
            return False
        return True
