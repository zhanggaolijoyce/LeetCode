# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findBottomLeftValue(self, root: Optional[TreeNode]) -> int:
        dq = deque([root])
        res = root.val
        while dq:
            for i in range(len(dq)):
                node = dq.popleft()
                if i == 0:
                    res = node.val
                if node.left:
                    dq.append(node.left)
                if node.right:
                    dq.append(node.right)
        return res
