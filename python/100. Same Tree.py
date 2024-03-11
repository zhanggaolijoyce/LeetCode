# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        ls1 = deque([p])
        ls2 = deque([q])
        while ls1 and ls2:
            i = ls1.popleft()
            j = ls2.popleft()
            if i == j == None:
                continue
            elif i == None and j != None:
                return False
            elif i != None and j == None:
                return False
            elif i.val != j.val:
                return False
            ls1.append(i.left)
            ls1.append(i.right)
            ls2.append(j.left)
            ls2.append(j.right)
        if ls1 or ls2:
            return False
        return True
