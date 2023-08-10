class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if nums == []:
            return 0
        m = k = 1
        for i in range(1, len(nums)):
            if nums[i] != nums[i-1]:
                k += 1
                nums[m] = nums[i]
                m += 1
        return k
