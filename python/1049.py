class Solution:
    def lastStoneWeightII(self, stones: List[int]) -> int:
        n = len(stones)
        s = sum(stones) // 2
        dp = [[0] * (s+1) for _ in range(n)]

        for i in range(s+1):
            if i >= stones[0]:
                dp[0][i] = stones[0]

        for i in range(1, n):
            for j in range(1, s+1):
                if j < stones[i]:
                    dp[i][j] = dp[i-1][j]
                else:
                    dp[i][j] = max(dp[i-1][j], dp[i-1][j-stones[i]]+stones[i])
        
        s1 = dp[n-1][s]
        s2 = sum(stones)-s1
        return s2-s1
