class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        n = len(s)
        res = 0
        i = n-1
        while  0 <=i < n and s[i] == ' ':
            i -= 1
        while 0 <=i < n and s[i]!=' ':
            res += 1
            i -= 1
        return res
