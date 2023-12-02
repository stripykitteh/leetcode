'''
Example 1:

Input: nums1 = [1,2,3,0,0,0], m = 3, nums2 = [2,5,6], n = 3
Output: [1,2,2,3,5,6]
Explanation: The arrays we are merging are [1,2,3] and [2,5,6].
The result of the merge is [1,2,2,3,5,6] with the underlined elements coming from nums1.
Example 2:

Input: nums1 = [1], m = 1, nums2 = [], n = 0
Output: [1]
Explanation: The arrays we are merging are [1] and [].
The result of the merge is [1].
Example 3:

Input: nums1 = [0], m = 0, nums2 = [1], n = 1
Output: [1]
Explanation: The arrays we are merging are [] and [1].
The result of the merge is [1].
Note that because m = 0, there are no elements in nums1. The 0 is only there to ensure the merge result can fit in nums1.
 

Constraints:

nums1.length == m + n
nums2.length == n
0 <= m, n <= 200
1 <= m + n <= 200
-109 <= nums1[i], nums2[j] <= 109
 

Follow up: Can you come up with an algorithm that runs in O(m + n) time?
'''

from typing import List

class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """

        '''
        pseudo-code
        iterate thru nums1 and nums2 simultaneously (maintain a pointer for each)
        if the value for the element of the nums1 offset is less, increment
        the nums1 offset
        if the value for the element of the nums2 offset is less, insert that
        element into nums1 (shifting the other values to the right), increment
        the nums2 offset and finally decrement the m-counter
        when the m-counter is zero we can return nums1 immediately
        '''

        ptr1 = 0
        ptr2 = 0
        while (ptr1 < (m+n)) and (ptr2 < n):
            print(ptr1, ptr2, nums1, nums2)
            # if we have reached the padded values, we
            # automatically insert the next nums2 element into nums1 and
            # increment both pointers
            if n - ptr2 >= m + n - ptr1:
                nums1.insert(ptr1, nums2[ptr2])
                nums1.pop()                
                ptr1 += 1
                ptr2 += 1
                continue
            # if nums1 element is less than or equal to nums2 element
            # just increment ptr1, otherwise insert the next nums2 element
            # and increment its pointer (but don't touch the ptr1 pointer)
            if nums1[ptr1] <= nums2[ptr2]:
                ptr1 += 1
            else:
                nums1.insert(ptr1, nums2[ptr2])
                nums1.pop()
                ptr2 += 1
        
if __name__ == '__main__':

    nums1 = [0]
    nums2 = [1]
    m = 0
    n = 1
    
    Solution().merge(nums1, m, nums2, n)
    print(nums1)
 
