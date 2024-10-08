# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        def dfs(node):
            if not node:
                return
            dfs(node.left)
            ls.append(node.val)
            dfs(node.right)

        ls = []
        dfs(root)
        if len(ls) <= 1:
            return 0
        res = inf
        for i in range(1, len(ls)):
            res = min(res, ls[i]-ls[i-1])

        return res
