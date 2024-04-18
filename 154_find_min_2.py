from typing import List

class Solution:

    def findMin(self, nums: List[int]) -> int:

        if len(nums) < 4:
            return min(nums)

        head = 0
        tail = len(nums) - 1
        mid = (head+tail) // 2

        '''
        Modified binary search.
        There are 10 cases to consider, where 0=min, 1=mid, 2=max,
        the brackets imply the new search range:
         1: (1 1 1) 
         2: (1) 1 2
         3: 1 (2 1)
         4: (2 1) 1
         5: 1 (1 0)
         6: (1 0) 1
         7: (0) 1 1
         8: (0) 1 2
         9: 1 (2 0)
        10: (2 0) 1

        The bastard case is (1 1 1), because [1,0,1,1,1] and [1,1,1,0,1] are
        both possible, as well as other nasty possibilities. We use recursion
        to handle the sub-ranges.
        '''
        #print(nums, head, mid, tail)
        if nums[head] == nums[mid] == nums[tail]: # Case 1
            if head == mid:
                return min(nums[head],nums[tail])
            else:
                return min(Solution.findMin(self,nums[head:mid+1]),
                           Solution.findMin(self,nums[mid:tail+1]))
        elif nums[head] == nums[mid] < nums[tail]: # Case 2
            return nums[head]
        elif nums[head] == nums[tail] < nums[mid]: # Case 3
            return Solution.findMin(self,nums[mid:tail+1])
        elif nums[head] > nums[mid] == nums[tail]: # Case 4
            return Solution.findMin(self,nums[head:mid+1])            
        elif nums[head] == nums[mid] > nums[tail]: # Case 5
            return Solution.findMin(self,nums[mid:tail+1])
        elif nums[head] == nums[tail] > nums[mid]: # Case 6
            return Solution.findMin(self,nums[head:mid+1])
        elif nums[head] < nums[mid] == nums[tail]: # Case 7
            return nums[head]
        elif nums[head] < nums[mid] < nums[tail]: # Case 8
            return nums[head]
        elif nums[tail] < nums[head] < nums[mid]: # Case 9
            return Solution.findMin(self,nums[mid:tail+1])
        else: # Case 10
            return Solution.findMin(self,nums[head:mid+1])

if __name__ == '__main__':

    nums = [1,3,5]    
    print(Solution().findMin(nums))
    nums = [2,2,2,0,1]
    print(Solution().findMin(nums))    
    nums = [-1,-1,-1,-1]
    print(Solution().findMin(nums))    

