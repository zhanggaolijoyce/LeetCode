class Solution:
    def divideArray(self, nums: List[int], k: int) -> List[List[int]]:
        nums = sorted(nums)
        res = []
        for i in range(0, len(nums), 3):
            ls=nums[i:i+3]
            if max(ls)-min(ls)>k:
                return []
            res.append(ls)
        return res
