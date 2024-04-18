import bisect

from typing import List

class Solution:

    def numberOfGoodPartitions(self, nums: List[int]) -> int:

        modulo = 10**9 + 7

        '''
        look at both ends of the list, make a note of elements seen
        if we have seen an element at both ends, we can remove the middle
        values
        e.g., [1,5,2,5,6] could be replaced with [1,5,6]
        but we also need to handle this: [1,5,1,5,6] => should be [1,6]
        '''
        seen = {}
        seen_twice = -1
        
        for i in range(0,len(nums)//2):
            if nums[i] in seen:
                if seen[nums[i]][0] == -1:
                    seen[nums[i]][0] = i
                if seen[nums[i]][1] != -1:
                    if seen_twice == -1:
                        seen_twice = nums[i]
                    elif seen[nums[i]][1] - seen[nums[i]][0] > seen[seen_twice][1] - seen[seen_twice][0]:
                        seen_twice = nums[i]                   
            else:
                seen[nums[i]] = [i,-1]
            if nums[len(nums) - i - 1] in seen:
                if seen[nums[len(nums) - i - 1]][1] == -1:
                    seen[nums[len(nums) - i - 1]][1] = len(nums) - i - 1
                if seen[nums[len(nums) - i - 1]][0] != -1:
                     if seen_twice == -1:
                        seen_twice = nums[len(nums) - i - 1] 
                     elif seen[nums[len(nums) - i - 1]][1] - seen[nums[len(nums) - i - 1]][0] > seen[seen_twice][1] - seen[seen_twice][0]:
                        seen_twice = nums[len(nums) - i - 1]
            else:
                seen[nums[len(nums) - i - 1]] = [-1,len(nums) - i - 1]

        #print("nums=>",nums,"seen=>",seen,"seen_twice=>",seen_twice)

        # if element from beginning or end seen in the seen_twice range, remove accordingly        
        if seen_twice > -1:
            low_range = seen[seen_twice][0]
            high_range = seen[seen_twice][1]
            for key in seen:
                if -1 < seen[key][0] < low_range:
                    if key in nums[seen[seen_twice][0]+1:seen[seen_twice][1]]:
                        #print(key, seen[key])                        
                        low_range = seen[key][0]
                if high_range < seen[key][1] < len(nums):
                    if key in nums[seen[seen_twice][0]+1:seen[seen_twice][1]]:
                        #print(key, seen[key])
                        high_range = seen[key][1]

            for i in range(0,low_range):
                if nums[i] in nums[low_range+1:seen[seen_twice][0]]:
                    low_range = i
                    break

            for j in range(len(nums)-1,high_range,-1):
                if nums[j] in nums[seen[seen_twice][1]+1:high_range]:
                    high_range = j
                    break
                
            # now remove the middle part
            nums = nums[0:low_range] + nums[high_range:len(nums)]

        #print("nums=>",nums)
        
        # if we encounter runs of the same element, we can throw out dupes
        index = 0

        while index < len(nums) - 1:
            if nums[index] == nums[index+1]:
                nums.pop(index)
                #print("nums=>",nums)
            else:
                index += 1

        # convert nums to a set and compare lengths, if equal we are done
        if len(set(nums)) == len(nums):
            return 2 ** (len(nums)-1) % modulo
                
        dict = {}
        part = []
        new_part = []
        
        for i in range(len(nums)):
            indices = [j for j, x in enumerate(nums) if x == nums[i]]
            dict[nums[i]] = indices

        #print("dict=>",dict)

        # create a separate partition for each key in dict
        for dict_key in dict:
            part.append((dict[dict_key][0], dict[dict_key][len(dict[dict_key])-1]))

        #print("part=>",part)

        old_len = len(part) + 1
        lets_skip = False
        
        while len(part) < old_len:
            for i in range(0,len(part)):
                #print("i=>",i,"part=>",part,"length=>",len(part))
                if lets_skip == True:
                    lets_skip = False
                elif i + 1 >= len(part):
                    new_part.append(part[i])     
                elif (part[i][0] < part[i+1][0] and part[i][1] > part[i+1][0]) or (part[i][0] < part[i+1][1] and part[i][1] > part[i+1][1]):
                    new_tuple = (min(part[i][0],part[i+1][0]), max(part[i][1],part[i+1][1]))
                    new_part.append(new_tuple)
                    lets_skip = True
                else:
                    new_part.append(part[i])
                #print("new_part=>",new_part)
            old_len = len(part)
            part = new_part
            new_part = []

        return 2 ** (len(part)-1) % modulo
            
if __name__ == '__main__':

    nums=[1,2,3,4,5,6,5,4,3,7,8,9]
    #print(Solution().numberOfGoodPartitions(nums))
    nums=[12,50,80,30,86,50,89,57,91,29]
    #print(Solution().numberOfGoodPartitions(nums))
    nums=[1,5,1,5,6]
    #print(Solution().numberOfGoodPartitions(nums))
    nums=[2,4,2,7,4]
    #print(Solution().numberOfGoodPartitions(nums))
    nums=[19,95,70,80,50,83,45,95,34,80]
    #print(Solution().numberOfGoodPartitions(nums))
    nums=[28,35,38,21,40,32,74,32,21,63]
    #print(Solution().numberOfGoodPartitions(nums))
    nums=[13,38,31,47,88,74,98,31,98,24]
    #print(Solution().numberOfGoodPartitions(nums))
    nums=[13,17,76,63,98,99,88,49,17,87,21,76,5,95,23,27,71,34,61,30,51,44,84,74,81,42,16,32,26,55,16,66,7,98,55,77,83,85,80,24,40,88,5,7,4,52,64,22,21,38,28,1,5,20,42,84,5,95,14,18,75,53,57,59,34,75,10,82,65,55,20,28,9,21,28,80,7,50,52,48,86,77,80,65,48,64,9,59,41,38,69,81,63,71,51,64,26,94,77,82]
    #print(Solution().numberOfGoodPartitions(nums))
    nums=[60,70,28,34,7,16,44,40,56,99,24,11,16,24,58]
    #print(Solution().numberOfGoodPartitions(nums))
    nums=[10,50,88,4,33,81,16,86,88,46,75,43,31,92,26,48,94,82,59,22,50,89,73,41,50,97,24,97,36,68,5,40,32,2,14,63,66,50,79,11,26,82,42,40,90,11,12,46,8,43,20,72,13,23,21,36,70,30,87,25,22,12,100,25,77,5,13,76,28,63,37,21,27,27,4,29,56,31,15,29,44,10,97,24,35,7,41,49,71,30,46,15,10,9,28,87,32,6,1,31]
    #print(Solution().numberOfGoodPartitions(nums))
    nums=[72,36,83,56,55,83,90,2,6,74,12,58,96,88,78,85,25,87,33,60,59,57,29,87,16,74,73,91,60,20,35,3,84,3,22,24,56,27,34,29,45,70,67,41,73,88,71,21,99,18,99,30,70,93,55,3,40,12,54,14,18,58,58,64,66,9,71,48,1,88,78,85,62,61,34,13,5,65,84,15,79,31,15,90,61,17,39,57,56,60,3,4,65,72,22,13,90,42,35,42]
    #print(Solution().numberOfGoodPartitions(nums))
    nums=[89,36,89,72,36,83,56,55,83,90,2,6,74,12,58,96,88,78,85,25,87,33,60,59,57,29,87,16,74,73,91,60,20,35,3,84,3,22,24,56,27,34,29,45,70,67,41,73,88,71,21,99,18,99,30,70,93,55,3,40,12,54,14,18,58,58,64,66,9,71,48,1,88,78,85,62,61,34,13,5,65,84,15,79,31,15,90,61,17,39,57,56,60,3,4,65,72,22,13,90,42,35,42]
    #print(Solution().numberOfGoodPartitions(nums))
