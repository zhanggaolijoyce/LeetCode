from random import randrange
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        def quicksort(nums, low, high):
            if low >= high:
                return

            r = low + randrange(high-low+1)
            nums[r], nums[low] = nums[low], nums[r]
            p = nums[low]
            m = low
            for i in range(low+1, high+1):
                if nums[i]>p or (nums[i]==p and randrange(2)==0):
                    m += 1
                    nums[i], nums[m] = nums[m], nums[i]
            nums[low], nums[m] = nums[m], nums[low]
            quicksort(nums, low, m-1)
            quicksort(nums, m+1, high)

            return nums
        
        quicksort(nums, 0, len(nums)-1)
        return nums[k-1]
