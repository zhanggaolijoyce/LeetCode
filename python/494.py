class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        s = sum(nums)
        if target < -s or target > s or (s+target)%2 :
            return 0
        k = (s+target)//2

        n = len(nums)
        dp = [[0]*(k+1) for _ in range(n)]
        
        if nums[0] <= k:
            dp[0][nums[0]] = 1

        t = 0
        for i in range(n):
            if nums[i] == 0:
                t += 1
            dp[i][0] = 2**t
        
        for i in range(1, n):
            for j in range(1, k+1):
                if j < nums[i]:
                    dp[i][j] = dp[i-1][j]
                else:
                    dp[i][j] = dp[i-1][j] + dp[i-1][j-nums[i]]

        return dp[n-1][k]
