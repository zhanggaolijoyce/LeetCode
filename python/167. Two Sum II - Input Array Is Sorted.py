class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        for k in range(len(numbers)-1, -1, -1):
            if numbers[k]+numbers[0]<=target:
                break

        for i in range(len(numbers)):
            j = k
            while i < j:
                if numbers[i]+numbers[j]>target:
                    j -= 1
                elif numbers[i]+numbers[j]<target:
                    break
                elif numbers[i]+numbers[j]==target:
                    return[i+1,j+1]
