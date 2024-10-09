# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findMode(self, root: Optional[TreeNode]) -> List[int]:
        def traversal(node):
            if not node:
                return
            traversal(node.left)
            ls.append(node.val)
            traversal(node.right)
        
        ls = []
        traversal(root)
        if not ls:
            return []
        max_t = 1
        res = [ls[0]]
        t = 1
        for i in range(1, len(ls)):
            if ls[i] != ls[i-1]:
                t = 1
            else:
                t += 1
            if t == max_t:
                res.append(ls[i])
            elif t > max_t:
                res = [ls[i]]
                max_t = t
        return res
