# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        if not root:
            return TreeNode(val)
        node = root
        while True:
            if not node.left and node.val > val:
                node.left = TreeNode(val)
                break
            if not node.right and node.val < val:
                node.right = TreeNode(val)
                break
            if node.val > val:
                node = node.left
            elif node.val < val:
                node = node.right
        return root
