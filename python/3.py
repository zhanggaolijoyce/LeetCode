class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) == 0:
            return 0
        dp = [1]*len(s)

        s1 = {s[0]}
        for i in range(1, len(s)):
            if s[i] in s1:
                break
            s1.add(s[i])
        dp[0] = len(s1)
        k = len(s1)

        for i in range(1, len(s)):
            s1.remove(s[i-1])
            dp[i] = dp[i-1]-1
            for j in range(k, len(s)):
                if s[j] in s1:
                    break
                s1.add(s[j])
                dp[i] += 1
                k += 1
        return max(dp)
