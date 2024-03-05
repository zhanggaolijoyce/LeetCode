class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        k = t = 1
        for i in range(1, len(nums)):
            if nums[i] == nums[i-1] and t == 2:
                continue
            elif nums[i] == nums[i-1]:
                nums[k] = nums[i]
                k += 1
                t += 1
            elif nums[i] != nums[i-1]:
                nums[k] = nums[i]
                k += 1
                t = 1
        return k
            
