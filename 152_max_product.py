from typing import List
import numpy
import sys

class Solution:

    def maxProduct(self, nums: List[int]) -> int:

        '''
        Find runs of integers that are not zero, and have an even number of
        negative integers.
        '''
        nums += [0] # guaranteed to have a zero
        
        size = len(nums)
        idx_list = [idx + 1 for idx, val in
                    enumerate(nums) if val == 0]

        res = [nums[i:j] for i, j in
               zip([0] + idx_list, idx_list +
                   ([size] if idx_list[-1] != size else []))]

        '''
        if there is a zero in nums then set best to zero otherwise make it a
        large negative number
        '''
        best = 0 if idx_list[0] < size else -sys.maxsize - 1
        for k in res:
            k = k[:-1] # remove trailing zero
            size_k = len(k)
            idx_list_k = [idx for idx, val in
                          enumerate(k) if val < 0]
            
            '''
            idx_list_k tells us where the -ve numbers are
            If there are an even number of them return the product of the
            whole list
            If there are an odd number, work out the products splitting either
            at the first -ve or the last -ve and return the highest
            '''
            if len(idx_list_k) % 2 == 0:
                best =  max(best, numpy.prod(k) if k else 0)
            else:
                best = max(best,
                           numpy.prod(k[:idx_list_k[0]]) if idx_list_k[0] > 0 else k[idx_list_k[0]],
                           numpy.prod(k[idx_list_k[0]+1:]) if idx_list_k[0] < len(k)-1 else k[idx_list_k[0]], 
                           numpy.prod(k[:idx_list_k[-1]]) if idx_list_k[-1] > 0 else k[idx_list_k[-1]],
                           numpy.prod(k[idx_list_k[-1]+1:]) if idx_list_k[-1] < len(k)-1 else k[idx_list_k[-1]])

        return best
    
if __name__ == '__main__':

    nums = [2,3,-2,4]
    print(Solution().maxProduct(nums))
    nums = [-2,0,-1]
    print(Solution().maxProduct(nums))    
    nums = [-2]
    print(Solution().maxProduct(nums))    
    nums = [0]
    print(Solution().maxProduct(nums))    
    nums = [3,-1,4]
    print(Solution().maxProduct(nums))    
