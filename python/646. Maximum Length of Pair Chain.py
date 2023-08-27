class Solution:
    def findLongestChain(self, pairs: List[List[int]]) -> int:
        pairs = sorted(pairs) # Sort pairs by the second element
        if len(pairs) <= 1:
            return len(pairs)
        
        dp = [1] * len(pairs)  # Initialize a dynamic programming array
        
        for i in range(1, len(pairs)):
            for j in range(i):
                if pairs[i][0] > pairs[j][1]:
                    dp[i] = max(dp[i], dp[j] + 1)
        
        return max(dp)
