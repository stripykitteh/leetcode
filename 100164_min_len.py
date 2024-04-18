from typing import List
from collections import Counter
from operator import itemgetter

class Solution:

    def minimumArrayLength(self, nums: List[int]) -> int:

        c = Counter(nums)

        min_key, min_count = min(c.items(), key=itemgetter(0))

        for key in c:
            if key != min_key and 0 < key % min_key < min_key:
                return 1

        return (min_count + 1) // 2

if __name__ == '__main__':

    nums = [1,4,3,1]
    print(Solution().minimumArrayLength(nums))
    nums = [5,5,5,10,5]
    print(Solution().minimumArrayLength(nums))
    nums = [2,3,4]
    print(Solution().minimumArrayLength(nums))
    nums = [7,7,7]
    print(Solution().minimumArrayLength(nums))
    nums = [11,11,11,11]
    print(Solution().minimumArrayLength(nums))
    nums = [13,13,13,13,13]
    print(Solution().minimumArrayLength(nums))
    nums = [5,2,2,2,9,10]
    print(Solution().minimumArrayLength(nums))



    
