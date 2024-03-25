class Solution:
    def longestPalindrome(self, s: str) -> str:
        res = [1]*len(s)
        for i in range(len(s)):
            for j in range(len(s)-1, -1, -1):
                if s[i] == s[j]:
                    m = i+1
                    n = j-1
                    same = True
                    while m<n:
                        if s[m]==s[n]:
                            m += 1
                            n -= 1
                        else:
                            same = False
                            break
                    if same:
                        res[i] = max(res[i], j-i+1)
                        break
        longest = max(res)
        index = res.index(longest)
        return s[index:index+longest]
