class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        s = sum(nums)
        if s % 2 != 0:
            return False
        target = s // 2
        n = len(nums)
        dp = [[0] * (target+1) for _ in range(n)]
        
        for i in range(1, target+1):
            if i >= nums[0]:
                dp[0][i] = nums[0]

        for i in range(1, n):
            for j in range(1, target+1):
                if j < nums[i]:
                    dp[i][j] = dp[i-1][j]
                else:
                    dp[i][j] = max(dp[i-1][j], dp[i-1][j-nums[i]]+nums[i])

        if dp[n-1][target] == target:
            return True
        return False
