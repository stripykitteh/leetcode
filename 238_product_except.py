from typing import List
import numpy

class Solution:

    def productExceptSelf(self, nums: List[int]) -> List[int]:    

        '''
        create a dict (of lists)
        iterate over nums
        add to dict with indices of numbers seen (-30 to 30)
        if we see 2 zeroes we are done (return a list of len(nums) zeroes)
        if we only have one zero then the ret_val at that index will be
        non-zero (all other entries will be zero)
        for each key in the dict count the times that number was seen (will be
        length of list for that key value) and calculate the power value
        '''

        length = len(nums)
        ret_val = []
        
        d, p, s = {}, {}, {}
        

        for i in range(length):
            if nums[i] in d:
                d[nums[i]].append(i)
                if nums[i] == 0:
                    return [0] * length
            else:
                d[nums[i]] = [i]
                
        for k in d:
            if k != 0:
                p[k] = k**len(d[k])

        for k in d:
            if k == 0:
                s[k] = numpy.prod([p[k] for k in p])
                continue
            if 0 in d:
                s[k] = 0
                continue
            p_tmp = p.pop(k)
            v = [p[k] for k in p]
            s[k] = (numpy.prod(v) if v else 1) * k**(len(d[k])-1)
            p[k] = p_tmp
                
        #print("d=>",d,"p=>",p, "s=>",s)

        for i in range(length):
            ret_val.append(s[nums[i]])
                
        return ret_val

if __name__ == '__main__':

    nums = [1,2,3,4]    
    print(Solution().productExceptSelf(nums))
    nums = [-1,-1,0,3,3]
    print(Solution().productExceptSelf(nums))
    nums = [0,0]
    print(Solution().productExceptSelf(nums))
    nums = [1,1]
    print(Solution().productExceptSelf(nums))
