# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        dq = deque()
        dq.append([root, 1])
        res = []
        while dq:
            node,l = dq.popleft()
            if l-1 < len(res):
                res[l-1].append(node.val)
            else:
                res.append([node.val])
            if node.left != None:
                dq.append([node.left, l+1])
            if node.right != None:
                dq.append([node.right, l+1])
        return res
