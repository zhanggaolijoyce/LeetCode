class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        n = len(nums)
        ls = [0]*n
        s = 0
        for i in range(n):
            s += nums[i]
            if s >= target:
                break
        
        if s < target and i == n-1:
            return 0
        
        ls[0] = i+1
        for j in range(1, n):
            s = s-nums[j-1]
            while i < n-1 and s < target:
                i += 1
                s += nums[i]
            if s >= target:
                ls[j] = i-j+1
        
        if all(x==0 for x in ls):
            return 0
        else:
            min = ls[0]
            for x in ls:
                if x < min and x != 0:
                    min = x
            return min
