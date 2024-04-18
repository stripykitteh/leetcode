from typing import List

class Solution:
    
    def divideArray(self, nums: List[int], k: int) -> List[List[int]]:

        nums.sort()

        ret_val = []
        
        for i in range(len(nums)//3):
            #print(nums[i*3], nums[i*3+1], nums[i*3+2])
            if nums[i*3+2] - nums[i*3] > k:
                ret_val = []                
                break
            else:
                ret_val += [[nums[i*3], nums[i*3+1], nums[i*3+2]]]

        #print(ret_val)
        
        return ret_val

if __name__ == '__main__':

    #nums = [1,3,4,8,7,9,3,5,1]
    #k = 2

    #nums = [1,3,3,2,7,3]
    #k = 3

    nums = [33,26,4,18,16,24,24,15,8,18,34,20,24,16,3]
    k = 16
    
    print(Solution().divideArray(nums, k))
