class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        n = len(nums)
        s = [0]*n
        for i in range(n):
            if s[nums[i]-1] == 0:
                s[nums[i]-1] = 1
            else:
                j = i
                continue
        k = s.index(0)
        return [nums[j], k + 1]
