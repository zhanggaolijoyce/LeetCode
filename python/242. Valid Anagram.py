class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        d = {}
        for letter in s:
            if letter in d:
                d[letter]+=1
            else:
                d[letter]=1
        for char in t:
            if char not in d:
                return False
            d[char] -= 1
            if d[char] == 0:
                del d[char]
        return False if d else True
