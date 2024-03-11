# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if root == None:
            return root
        q = deque([root])
        while q:
            ele = q.popleft()
            temp = ele.left
            ele.left = ele.right
            ele.right = temp
            if ele.left != None:
                q.append(ele.left)
            if ele.right != None:
                q.append(ele.right)
        return root
