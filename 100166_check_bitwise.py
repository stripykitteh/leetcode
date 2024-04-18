import numpy as np

from typing import List

class Solution:
    def hasTrailingZeros(self, nums: List[int]) -> bool:

        count = 0

        for i in range(len(nums)):
            if nums[i] % 2 == 0:
                count += 1
                if count >= 2:
                    return True

        return False

if __name__ == '__main__':

    nums = [1,2,3,4,5]
    print(Solution().hasTrailingZeros(nums))
