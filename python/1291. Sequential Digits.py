class Solution:
    def sequentialDigits(self, low: int, high: int) -> List[int]:
        n = m = 1
        while(low/(10**n) >= 1 ):
            n += 1

        while(high/(10**m) >= 1 ):
            m += 1
        
        res = []
        
        for k in range(n, m+1):
            for p in range(1, 10):
                if p*10**(k-1) > high:
                    break
                if p+k-1 > 9:
                    break
                num = 0
                for i in range(0, k):
                    num += (p+i)*10**(k-1-i)
                if low <= num <= high:
                    res.append(num)
                elif num > high:
                    break
        return res
