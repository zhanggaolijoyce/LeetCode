class Solution:
    def climbStairs(self, n: int) -> int:
        memo={1:1, 2:2}
        for i in range(1, n+1):
            if i in memo:
                continue
            memo[i] = memo[i-1]+memo[i-2]
        return memo[n]
