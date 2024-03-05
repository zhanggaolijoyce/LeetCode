class Solution:
    def isPalindrome(self, s: str) -> bool:
        s1 = []
        for i in range(len(s)):
            if 97<=ord(s[i])<=122 or 48<=ord(s[i])<=57:
                s1.append(s[i])
            elif 65<=ord(s[i])<=90:
                s1.append(chr(ord(s[i])+32))
        i = 0
        j = len(s1)-1
        while i < j:
            if s1[i] != s1[j]:
                return False
            else:
                i += 1
                j -= 1
        return True
