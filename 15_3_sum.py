from typing import List
import logging, sys, random
from itertools import combinations

logging.basicConfig(stream=sys.stdout, level=logging.WARNING)

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:

        nums.sort()
        logging.debug(nums)
        ret_val = []

        i,neg = 0,[] 
        while nums[i] < 0:
            if i >= 2:
                if not(nums[i] == nums[i-1] and nums[i] == nums[i-2]):
                    neg.append(nums[i])
            else:
                neg.append(nums[i])                
            i += 1

        logging.debug("step 1, %s",neg)
        
        zero_count,zero_start = 0,i
        while i < len(nums) and nums[i] == 0:
            zero_count += 1
            i += 1

        logging.debug("step 2, %s",zero_count)
        
        pos = []
        while i < len(nums):
            if i >= 2:
                if not(nums[i] == nums[i-1] == nums[i-2]):
                    pos.append(nums[i])
            else:
                pos.append(nums[i])
            i += 1
            
        logging.debug("step 3, %s",pos)
        
        # 3 zeroes
        if zero_count >= 3:
            ret_val.append([0,0,0])

        logging.debug("step 4, %s",ret_val)

        # 1 zero
        if zero_count >= 1:                
            left, right = 0, len(pos)-1
            while left < len(neg) and right >= 0:
                current = neg[left] + pos[right]
                logging.debug("%s,%s,%s",left,right,current)
                if current == 0:
                    if [neg[left],0,pos[right]] not in ret_val:
                        ret_val.append([neg[left],0,pos[right]])
                    right -= 1
                    left += 1
                elif current > 0:
                    right -= 1
                else:
                    left += 1

        logging.debug("step 5, %s",ret_val)                    

        # no zeroes
        for x,y in combinations(pos,2):
            target = -(x+y)
            logging.debug("%s,%s,%s",x,y,target)
            if target in neg:
                ret_val.append([target,x,y])
        logging.debug("step 6, %s",ret_val)                    
                    
        for x,y in combinations(neg,2):
            target = -(x+y)
            logging.debug("%s,%s,%s",x,y,target)
            if target in pos:
                ret_val.append([x,y,target])

        return ret_val

    
if __name__ == '__main__':

    nums = [-1,0,1,2,-1,-4]
    print(Solution().threeSum(nums))    
    nums = [0,1,1]
    print(Solution().threeSum(nums))    
    nums = [0,0,0]
    print(Solution().threeSum(nums))    
    nums = [1,1,-2]
    print(Solution().threeSum(nums))    
    nums = [-1,0,1]
    print(Solution().threeSum(nums))    
    nums = [-4,-2,-2,-2,0,1,2,2,2,3,3,4,4,6,6]
    print(Solution().threeSum(nums))    
    #nums = [34,55,79,28,46,33,2,48,31,-3,84,71,52,-3,93,15,21,-43,57,-6,86,56,94,74,83,-14,28,-66,46,-49,62,-11,43,65,77,12,47,61,26,1,13,29,55,-82,76,26,15,-29,36,-29,10,-70,69,17,49]
    #print(Solution().threeSum(nums))    
    nums = [-2,-3,0,0,-2]    
    print(Solution().threeSum(nums))
    random_list = random.sample(range(-100000,100000),3000)
    print(Solution().threeSum(random_list))    
