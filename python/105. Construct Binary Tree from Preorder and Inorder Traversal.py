# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        if not inorder:
            return None
        node = TreeNode(preorder[0])
        id = inorder.index(preorder[0])
        node.left = self.buildTree(preorder[1:], inorder[:id])
        node.right = self.buildTree(preorder[id+1:], inorder[id+1:])
        return node
