class Solution:
    def romanToInt(self, s: str) -> int:
        ls = ["I", "V", "X", "L", "C", "D", "M"]
        value = [1, 5, 10, 50, 100, 500, 1000]
        l = len(s)
        res = value[ls.index(s[-1])]
        for i in range(l-2, -1, -1):
            if ls.index(s[i]) >= ls.index(s[i+1]):
                res += value[ls.index(s[i])]
            else:
                res -= value[ls.index(s[i])]
        return res
