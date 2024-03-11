# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        if root == None:
            return True
        ls = [[root]]
        q = deque()
        q.append((root, 1))
        while q:
            ele, l = q.popleft()
            if ele == None:
                continue
            q.append((ele.left, l+1))
            q.append((ele.right, l+1))
            if l == len(ls):
                ls.append([])
                ls[l].append(ele.left)
                ls[l].append(ele.right)
            elif l < len(ls):
                ls[l].append(ele.left)
                ls[l].append(ele.right)
        
        for row in ls[1:]:
            l1 = len(row)
            for i in range(0, l1//2):
                if row[i] == None and row[l1-i-1] != None:
                    return False
                if row[i] != None and row[l1-i-1] == None:
                    return False
                if row[i] == row[l1-i-1] == None:
                    continue
                if row[i].val != row[l1-i-1].val:
                    return False
        return True
