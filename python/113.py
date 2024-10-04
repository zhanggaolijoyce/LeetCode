# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        def count(node, s, path):
            if not node:
                return
            path.append(node.val)
            if (not node.left) and (not node.right) and node.val == s:
                res.append(path[:])
            count(node.left, s-node.val, path)
            count(node.right, s-node.val, path)
            path.pop()

        
        res = []
        count(root, targetSum, [])
        return res
