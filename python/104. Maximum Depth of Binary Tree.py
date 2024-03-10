# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        s = deque()
        s.append((root, 1))

        while s:
            ele,l = s.popleft()
            if ele.left != None:
                s.append((ele.left, l+1))
            if ele.right != None:
                s.append((ele.right, l+1))
        return l
