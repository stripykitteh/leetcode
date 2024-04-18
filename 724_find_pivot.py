from typing import List

class Solution:

    def pivotIndex(self, nums: List[int]) -> int:        

        l = 0
        if len(nums) > 1:
            r = sum(nums[1:])
        else:
            r = 0

        if l == r:
            return 0
        
        for i in range(0,len(nums)-1):
            l += nums[i]
            r -= nums[i+1]
            if l == r:
                return i+1
            
        return -1

if __name__ == '__main__':

    nums = [1,7,3,6,5,6]
    print(Solution().pivotIndex(nums))
    nums = [1,2,3]
    print(Solution().pivotIndex(nums))    
    nums = [2,1,-1]
    print(Solution().pivotIndex(nums))
    nums = [-1,-1,0,1,1,0]    
    print(Solution().pivotIndex(nums))
    nums = [0]    
    print(Solution().pivotIndex(nums))
