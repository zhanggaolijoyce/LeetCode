class Solution:
    def getFinalState(self, nums: List[int], k: int, multiplier: int) -> List[int]:
        if multiplier == 1:
            return nums

        p = max(nums)
        n = len(nums)
        hq = []
        for idx, num in enumerate(nums):
            heapq.heappush(hq, [num, idx])

        while k:
            if hq[0][0] * multiplier > p and k >= n:
                for i in range(n):
                    hq[i][0] *= pow(multiplier, k // n, 10**9 + 7)
                p *= k//n
                k = k % n
            else:
                num, idx = heapq.heappop(hq)
                heapq.heappush(hq, [num*multiplier, idx])
                k -= 1
                p = max(p, num*multiplier)
        res = [0]*n
        for num, idx in hq:
            res[idx] = num%(10**9 + 7)
        return res

        
