class Solution:
    def mySqrt(self, x: int) -> int:
        if x<=1:
            return x
        a = 0
        b = x
        mid = (a+b)//2
        while mid != a and mid != b:
            if mid*mid == x:
                return mid
            elif mid*mid > x:
                b = mid
                mid = (a+b)//2
            else:
                a = mid
                mid = (a+b)//2
        return mid
