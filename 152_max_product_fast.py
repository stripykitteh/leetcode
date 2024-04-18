from typing import List
import numpy
import sys

class Solution:

    def maxProduct(self, nums: List[int]) -> int:
        curMax, curMin = 1, 1
        res = nums[0]
        
        for n in nums:
            vals = (n, n * curMax, n * curMin)
            curMax, curMin = max(vals), min(vals)
	    
            res = max(res, curMax)

            print("res=>",res,"vals=>",vals,"curMax=>",curMax,"curMin=>",curMin)
            
        return res
    
if __name__ == '__main__':

    nums = [2,3,-2,4]
    print(Solution().maxProduct(nums))
    nums = [-2,0,-1]
    print(Solution().maxProduct(nums))    
    nums = [-2]
    print(Solution().maxProduct(nums))    
    nums = [0]
    print(Solution().maxProduct(nums))    
    nums = [3,-1,4]
    print(Solution().maxProduct(nums))    
