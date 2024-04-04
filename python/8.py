class Solution:
    def myAtoi(self, s: str) -> int:
        if not s:
            return 0
        res = "0"
        sigh = 1
        i = 0
        j = 0
        while i<len(s) and j<len(s):
            for i in range(j, len(s)):
                if s[i] == ' ':
                    continue
                if s[i] == "+":
                    sigh = 1
                    i += 1
                    break
                if s[i] == "-":
                    sigh = -1
                    i += 1
                    break
                if s[i].isdigit():
                    break
                else:
                    return sigh*int(res)
            
            for j in range(i, len(s)):
                if not s[j].isdigit():
                    return 0
                while j < len(s) and s[j].isdigit():
                    res += s[j]
                    j += 1
                res = sigh * int(res)
                if sigh == 1:
                    return min(res, 2**31-1)
                else:
                    return max(res, -2**31)
        return 0
                
