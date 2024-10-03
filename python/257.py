# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        def path(node, p):
            if not node:
                return
            p.append(str(node.val))
            if (not node.left) and (not node.right):
                res.append("->".join(p))
                
            path(node.left, p)
            path(node.right, p)
            p.pop()

        res = []
        if not root:
            return []
        path(root, [])
        return res
