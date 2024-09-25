class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        n = len(nums)
        res = []
        for a in range(n):
            if a > 0 and nums[a] == nums[a - 1]:
                continue
            for b in range(a+1, n):
                if b > a+1 and nums[b] == nums[b-1]:
                    continue
                d = n - 1
                for c in range(b+1, n):
                    if c > b+1 and nums[c] == nums[c-1]:
                        continue
                    rest = target - nums[a] - nums[b]
                    while c < d and nums[c] + nums[d] > rest:
                        d -= 1
                    if c == d:
                        break
                    if nums[c] + nums[d] == rest:
                        res.append([nums[a], nums[b], nums[c], nums[d]])
        return res
