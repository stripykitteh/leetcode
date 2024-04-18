from typing import List

class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:

        s = sum(nums[0:k])
        b = s

        for i in range(1,len(nums) - k + 1):
            s = s - nums[i-1] + nums[i+k-1]
            b = max(b,s)
             
        return b/k
    
    
if __name__ == '__main__':

    nums, k = [1,12,-5,-6,50,3], 4
    print(Solution().findMaxAverage(nums, k))
    nums,k = [5], 1
    print(Solution().findMaxAverage(nums, k))
