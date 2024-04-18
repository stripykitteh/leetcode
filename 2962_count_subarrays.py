import bisect

from typing import List

class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:

        max_element = max(nums)

        #print("max_element=>", max_element)

        indices = [i for i, x in enumerate(nums) if x == max_element]

        #print("indices=>",indices)

        subarray_count = 0
        
        for i in range(len(nums)):
            # first element greater than or equal to the index
            first_subindex = bisect.bisect_left(indices, i)
            second_subindex = first_subindex + k - 1
            #print("i=>", i, "first_subindex=>", first_subindex, "second_subindex=>", second_subindex, "subarray_count=>", subarray_count)
            if second_subindex > len(indices) - 1:
                break
            else:
                subarray_count += len(nums) - indices[second_subindex]
    
        return subarray_count
        
if __name__ == '__main__':

    nums = [1,3,2,3,3]
    k = 2
    print(Solution().countSubarrays(nums, k))
    nums = [1,4,2,1]
    k = 3
    print(Solution().countSubarrays(nums, k))    
    nums = [1,4,2,1]
    k = 3
    print(Solution().countSubarrays(nums, k))    

