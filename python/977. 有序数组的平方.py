class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        l, r = 0, len(nums)-1
        res = [0]*len(nums)
        k = r
        while l <= r:
            if nums[l] * nums[l] >= nums[r] * nums[r]:
                res[k] = nums[l] * nums[l]
                l += 1
            else:
                res[k] = nums[r] * nums[r]
                r -= 1
            k -= 1
        return res
