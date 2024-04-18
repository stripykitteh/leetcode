from typing import List

class Solution:
    def numberOfGoodPartitions(self, nums: List[int], cnt = 0) -> int:

        d, s = {num:i for i, num in enumerate(nums)}, set()

        for i, num in enumerate(nums):
            s.add(num)
            if d[num] == i: s.remove(num)
            cnt+= (len(s) == 0)
            
        return pow(2, cnt - 1, 1_000_000_007)

if __name__ == '__main__':

    nums=[1,2,3,4,5,6,5,4,3,7,8,9]
    print(Solution().numberOfGoodPartitions(nums))
    nums=[12,50,80,30,86,50,89,57,91,29]
    print(Solution().numberOfGoodPartitions(nums))
    nums=[1,5,1,5,6]
    print(Solution().numberOfGoodPartitions(nums))
    nums=[2,4,2,7,4]
    print(Solution().numberOfGoodPartitions(nums))
   
