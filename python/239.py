class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        res = []
        ls = deque()
        for i in range(k):
            while ls and ls[-1] < nums[i]:
                ls.pop()
            ls.append(nums[i])
        res.append(ls[0])

        j = k
        for i in range(1, len(nums)-k+1):
            if nums[i-1] == ls[0]:
                ls.popleft()
            while ls and ls[-1] < nums[j]:
                ls.pop()
            ls.append(nums[j])
            j += 1
            res.append(ls[0])
        return res
