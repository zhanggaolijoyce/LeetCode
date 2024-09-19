class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        i = j = 0
        s = 0
        if sum(nums) < target:
            return 0
        min_l = len(nums)
        while i <= j < len(nums):
            s += nums[j]
            while i<=j and s >= target:
                min_l = min(min_l, j-i+1)
                s -= nums[i]
                i += 1
            if i > j:
                return 1
            j += 1
        return min_l

