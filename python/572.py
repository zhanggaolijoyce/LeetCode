# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        def compare(node1, node2):
            if not node1 and not node2:
                return True
            if not node1 or not node2:
                return False
            if node1.val != node2.val:
                return False
            return compare(node1.left, node2.left) and compare(node1.right, node2.right)

        dq= deque([root])
        while dq:
            node = dq.popleft()
            if compare(node, subRoot):
                return True
            if node.left:
                dq.append(node.left)
            if node.right:
                dq.append(node.right)
        return False
