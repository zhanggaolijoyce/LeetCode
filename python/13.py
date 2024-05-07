class Solution:
    def romanToInt(self, s: str) -> int:
        d = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000
        }

        n = len(s)
        res = 0
        i = 0
        while i < n:
            if i < n-1:
                if s[i] == "I" and s[i+1] == "V":   
                    res += 4
                    i += 2
                    continue
                if s[i] == "I" and s[i+1] == "X":
                    res += 9
                    i += 2
                    continue
                if s[i] == "X" and s[i+1] == "L":
                    res += 40
                    i += 2
                    continue
                if s[i] == "X" and s[i+1] == "C":
                    res += 90
                    i += 2
                    continue
                if s[i] == "C" and s[i+1] == "D":
                    res += 400
                    i += 2
                    continue
                if s[i] == "C" and s[i+1] == "M":
                    res += 900
                    i += 2
                    continue
                
            res += d[s[i]]
            i += 1
        return res
