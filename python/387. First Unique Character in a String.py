class Solution:
    def firstUniqChar(self, s: str) -> int:
        l = len(s)
        visited = set()
        for i in range(0, l):
            if s[i] in visited:
                continue
            res = True
            for j in range(i+1, l):
                if s[j] == s[i]:
                    res = False
                    visited.add(s[i])
                    break
            if res:
                return i
        return -1
