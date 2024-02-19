class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        if n <= 0:
            return False
        if n == 1:
            return True
        a = 1
        res = False
        while a <= n:
            if a == n:
                return True
            a *= 2
        if not res:
            return False
