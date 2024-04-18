from typing import List

from collections import Counter

class Solution:
    def maxFrequencyElements(self, nums: List[int]) -> int:

        d = Counter(nums)

        d_sorted = sorted(d, key=d.get, reverse=True)

        ret_val = 0
        best = 0
        old_best = 0
        for r in d_sorted:
            if best == 0:
                best = d[r]
            #print(best,old_best)
            if d[r] < best:
                return ret_val
            else:
                ret_val += d[r]

        return ret_val
    
if __name__ == '__main__':

    nums = [1,2,2,1,3,4]
    print(Solution().maxFrequencyElements(nums))
    nums = [1,2,3,4,5]
    print(Solution().maxFrequencyElements(nums))

