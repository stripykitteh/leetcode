from typing import List
from collections import Counter
from operator import itemgetter

class Solution:

    def minimumCost(self, nums: List[int], k: int, dist: int) -> int:

        d = {}

        for i in range(1,len(nums)):
            d[i] = nums[i]

        d_s = {k: v for k, v in sorted(d.items(), key=lambda item: item[1])}

        print(d_s)

        return 0

if __name__ == '__main__':

    nums, k, dist = [1,3,2,6,4,2],3,3
    print(Solution().minimumCost(nums,k,dist))    
    nums, k, dist = [10,1,2,2,2,1],4,3
    print(Solution().minimumCost(nums,k,dist))    
    nums, k, dist = [10,8,18,9],3,1
    print(Solution().minimumCost(nums,k,dist))



    
