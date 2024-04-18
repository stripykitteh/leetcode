from typing import List

class Solution:
    
    def maxOperations(self, nums: List[int], k: int) -> int:

        s_n = sorted(nums)
        l_s = len(s_n)
        l = 0
        r = l_s - 1
        c = 0
        while l < r:
            a = s_n[l] + s_n[r]
            if a < k:
                l += 1
            elif a == k:
                c += 1
                l += 1
                r -= 1
            else:
                r -= 1
            
        return c
    
if __name__ == '__main__':

    nums, k = [1,2,3,4], 5
    print(Solution().maxOperations(nums, k))
    nums, k = [3,1,3,4,3], 6
    print(Solution().maxOperations(nums, k))    
