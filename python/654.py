# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def constructMaximumBinaryTree(self, nums: List[int]) -> Optional[TreeNode]:
        def findRoot(nums):
            if not nums:
                return
            val = max(nums)
            idx = nums.index(val)
            root = TreeNode(val)
            root.left = findRoot(nums[:idx])
            root.right = findRoot(nums[idx+1 :])
            return root
        root = findRoot(nums)
        return root
