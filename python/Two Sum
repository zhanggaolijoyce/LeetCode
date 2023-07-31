class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        l = len(nums)
        numsSet = set(nums)
        for i in range(l):
            rest = target-nums[i]
            if rest in numsSet and rest != nums[i]:
                j = nums.index(rest)
                return [i, j]
            elif rest in numsSet:
                if nums.count(rest) == 2:
                    for j in range(i+1, l):
                        if nums[j] == rest:
                            return [i, j]
