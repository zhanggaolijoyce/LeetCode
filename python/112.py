# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        def count(node, s):
            if not node:
                return False
            if (not node.left) and (not node.right) and node.val == s:
                return True
            return count(node.left, s - node.val) or count(node.right, s - node.val)

        if not root:
            return False
        return count(root, targetSum)
