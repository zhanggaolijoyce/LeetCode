class Solution:
    def fourSumCount(self, nums1: List[int], nums2: List[int], nums3: List[int], nums4: List[int]) -> int:
        d1 = {}
        n = len(nums1)
        for i in range(n):
            for j in range(n):
                s = nums1[i] + nums2[j]
                d1[s] = d1.get(s, 0) + 1
        d2 = {}
        for i in range(n):
            for j in range(n):
                s = nums3[i] + nums4[j]
                d2[s] = d2.get(s, 0) + 1
    
        res = 0
        for v1 in d1:
            v2 = -v1
            if v2 in d2:
                res += d1[v1] * d2[v2]
        return res
