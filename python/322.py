class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        n = len(coins)
        dp = [[inf] * (amount+1) for _ in range(n)]

        for i in range(n):
            dp[i][0] = 0

        for j in range(1, amount+1):
            if j >= coins[0] and dp[0][j-coins[0]] != inf:
                dp[0][j] = dp[0][j-coins[0]] + 1

        for i in range(1,n):
            for j in range(1, amount+1):
                if j >= coins[i] and dp[i][j-coins[i]] != inf:
                    dp[i][j] = min(dp[i-1][j], dp[i][j-coins[i]]+1)
                else:
                    dp[i][j] = dp[i-1][j]

        return dp[n-1][amount] if dp[n-1][amount] != inf else -1
