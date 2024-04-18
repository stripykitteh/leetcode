import numpy as np

from typing import List

class Solution:
    def numberGame(self, nums: List[int]) -> List[int]:

        arr = []
        nums.sort()

        for i in range(0,len(nums),2):
            arr.append(nums[i+1])
            arr.append(nums[i])            
            
        return arr
                

if __name__ == '__main__':

    #nums = [5,2,4,3]
    #nums = [5,2]
    nums = [7,8,9,5,14,5]    
    
    print(Solution().numberGame(nums))



        
