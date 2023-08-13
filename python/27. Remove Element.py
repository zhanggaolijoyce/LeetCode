class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        m = k = 0
        for i in range(0, len(nums)):
            if nums[i] != val:
                k += 1
                nums[m] = nums[i]
                m += 1
        return k
