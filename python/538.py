# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def convertBST(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        def count(node):
            nonlocal s
            if not node:
                return
            count(node.right)
            s += node.val
            node.val = s
            count(node.left)

        s = 0
        count(root)
        
        return root
