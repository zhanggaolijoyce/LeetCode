class Solution:
    def isPalindrome(self, x: int) -> bool:
        x = str(x)
        for i in range(len(x)//2):
            j = len(x) - i - 1
            if x[i] != x[j]:
                return False
        return True
    
