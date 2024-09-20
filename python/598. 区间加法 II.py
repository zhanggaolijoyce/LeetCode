class Solution:
    def maxCount(self, m: int, n: int, ops: List[List[int]]) -> int:
        if ops == []:
            return m*n
        a, b = ops[0]
        for i in range(1, len(ops)):
            a = min(a, ops[i][0])
            b = min(b, ops[i][1])
        return a*b
