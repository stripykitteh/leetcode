from typing import List
import random
from itertools import combinations

#logging.basicConfig(stream=sys.stdout, level=logging.WARNING)

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:

        nums.sort()
        ret_val = []

        i,neg = 0,[] 
        while nums[i] < 0:
            if i >= 2:
                if not(nums[i] == nums[i-1] and nums[i] == nums[i-2]):
                    neg.append(nums[i])
            else:
                neg.append(nums[i])                
            i += 1

        zero_count,zero_start = 0,i
        while i < len(nums) and nums[i] == 0:
            zero_count += 1
            i += 1

        pos = []
        while i < len(nums):
            if i >= 2:
                if not(nums[i] == nums[i-1] == nums[i-2]):
                    pos.append(nums[i])
            else:
                pos.append(nums[i])
            i += 1
            
        # 3 zeroes
        if zero_count >= 3:
            ret_val.append([0,0,0])

        # 1 zero
        if zero_count >= 1:                
            left, right = 0, len(pos)-1
            while left < len(neg) and right >= 0:
                current = neg[left] + pos[right]
                if current == 0:
                    if [neg[left],0,pos[right]] not in ret_val:
                        ret_val.append([neg[left],0,pos[right]])
                    right -= 1
                    left += 1
                elif current > 0:
                    right -= 1
                else:
                    left += 1

        # no zeroes
        neg_ptr = len(neg)-1
        last_x = 0
        for x,y in combinations(pos,2):
            target = -(x+y)
            if x != last_x:
                neg_ptr = len(neg)-1
            while neg_ptr > -1 and neg[neg_ptr] >= target:
                if neg[neg_ptr] == target:
                    if [target,x,y] not in ret_val:
                        ret_val.append([target,x,y])
                    break
                elif neg[neg_ptr] < target:
                    break
                if neg_ptr > -1:
                    neg_ptr -= 1
            last_x = x

        pos_ptr = len(pos)-1
        last_x = 0
        for x,y in combinations(neg,2):
            target = -(x+y)
            if x != last_x:
                pos_ptr = len(pos)-1
            while pos_ptr > -1 and pos[pos_ptr] >= target:
                if pos[pos_ptr] == target:
                    if [x,y,target] not in ret_val:
                        ret_val.append([x,y,target])
                    break
                elif pos[pos_ptr] < target:
                    break
                if pos_ptr > -1:
                    pos_ptr -= 1
            last_x = x

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
    nums = [34,55,79,28,46,33,2,48,31,-3,84,71,52,-3,93,15,21,-43,57,-6,86,56,94,74,83,-14,28,-66,46,-49,62,-11,43,65,77,12,47,61,26,1,13,29,55,-82,76,26,15,-29,36,-29,10,-70,69,17,49]
    print(Solution().threeSum(nums))    
    nums = [-2,-3,0,0,-2]    
    print(Solution().threeSum(nums))
    random_list = random.sample(range(-100000,100000),3000)
    print(Solution().threeSum(random_list))    