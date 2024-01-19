class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        def neighbor(a, b):
            res = []
            res.append([a-1, b])
            if b > 0:
                res.append([a-1, b-1])
            if b < n-1:
                res.append([a-1, b+1])
            return res
    
        n = len(matrix)
        for i in range(1,n):
            for j in range(0, n):
                s = inf
                for ele in neighbor(i, j):
                    if matrix[ele[0]][ele[1]] + matrix[i][j] < s:
                        s = matrix[ele[0]][ele[1]] + matrix[i][j]
                matrix[i][j] = s
        return min(matrix[n-1])
