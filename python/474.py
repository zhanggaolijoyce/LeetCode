class Solution:
    def findMaxForm(self, strs: List[str], m: int, n: int) -> int:
        def countZero(str):
            n = str.count("0")
            return n

        l = len(strs)
        dp = [[[0] * (n+1) for _ in range(m+1)] for _ in range(l)]
        
        a = countZero(strs[0])
        b = len(strs[0]) - a
        for i in range(m+1):
            for j in range(n+1):
                if i>=a and j>=b:
                    dp[0][i][j] = 1
        
        for i in range(1, l):
            for j in range(m+1):
                for k in range(n+1):
                    a = countZero(strs[i])
                    b = len(strs[i]) - a
                    if j>=a and k>=b:
                        dp[i][j][k] = max(dp[i-1][j][k], dp[i-1][j-a][k-b]+1)
                    else:
                        dp[i][j][k] = dp[i-1][j][k]

        return dp[l-1][m][n]

