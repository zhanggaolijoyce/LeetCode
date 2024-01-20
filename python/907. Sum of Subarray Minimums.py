#Time Limit Exceeded in testcase77
class Solution:
    def sumSubarrayMins(self, arr: List[int]) -> int:
        res = sum(arr)
        n = len(arr)
        arr1 = arr[:]
        for i in range(1, n):
            for j in range(0, n-i):
                if arr1[j] > arr[j+i]:
                    arr1[j] = arr[j+i]
                res += arr1[j]    
               
        return res%(10**9 + 7)

  
