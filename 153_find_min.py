from typing import List

class Solution:

    def findMin(self, nums: List[int]) -> int:

        # binary search
        head = 0
        tail = len(nums) - 1
        mid = (head+tail) // 2
        
        while True:
            if nums[mid] > nums[tail]:
                head = mid
            else:
                tail = mid
            mid = (head+tail) // 2
            if head == mid:
                return min(nums[head],nums[tail])
    
if __name__ == '__main__':

    nums = [3,4,5,1,2]    
    print(Solution().findMin(nums))
    nums = [4,5,6,7,0,1,2]
    print(Solution().findMin(nums))    
    nums = [11,13,15,17]
    print(Solution().findMin(nums))    
