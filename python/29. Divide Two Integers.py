class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        sign = -1 if ((dividend>0 and divisor < 0) or (dividend<0 and divisor>0)) else 1
        dividend = abs(dividend)
        divisor = abs(divisor)
        k = len(range(0, dividend-divisor+1, divisor))
        return min(k, 2**31-1) if sign == 1 else max(-k, -2**31)
