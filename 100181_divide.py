from typing import List
import sys

class Solution:
    def minimumCost(self, nums: List[int]) -> int:

        s = sorted(nums[1:])

        return nums[0] + s[0] + s[1]

if __name__ == '__main__':

    nums = [1,2,3,12]
    print(Solution().minimumCost(nums))
    nums = [5,4,3]
    print(Solution().minimumCost(nums))
    nums = [10,3,1,1]
    print(Solution().minimumCost(nums))

    
