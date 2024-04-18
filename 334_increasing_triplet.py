from typing import List
import bisect
import sys

class Solution:

    def increasingTriplet(self, nums: List[int]) -> bool:

        l1, l2 = sys.maxsize - 1, sys.maxsize - 1
        
        for i in nums:
            if i < l1:
                l1 = i
            elif l1 < i < l2:
                l2 = i
            elif i > l2:
                return True
        
        return False
    
if __name__ == '__main__':

    nums = [1,2,3,4,5]    
    print(Solution().increasingTriplet(nums))
    nums = [5,4,3,2,1]
    print(Solution().increasingTriplet(nums))    
    nums = [2,1,5,0,4,6]
    print(Solution().increasingTriplet(nums))
    nums = [20,100,10,12,5,13]
    print(Solution().increasingTriplet(nums))
    nums = [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]    
    print(Solution().increasingTriplet(nums))
    nums = [5,1,6]
    print(Solution().increasingTriplet(nums))
    nums = [2,1,5,0,3]
    print(Solution().increasingTriplet(nums))
    nums = [1,5,0,4,1,3]
    print(Solution().increasingTriplet(nums))
    nums = [1,1,-2,6]
    print(Solution().increasingTriplet(nums))
