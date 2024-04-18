from typing import List

class Solution:

    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:

        set1 = set(nums1)
        set2 = set(nums2)

        ret1 = []

        for i in set1:
            if i not in set2:
                ret1.append(i)
            else:
                # we can remove items seen from set2                
                set2.remove(i)                

        return[ret1,list(ret2)]

if __name__ == '__main__':

    nums1 = [1,2,3]
    nums2 = [2,4,6]
    print(Solution().findDifference(nums1,nums2))

    nums1 = [1,2,3,3]
    nums2 = [1,1,2,2]
    print(Solution().findDifference(nums1,nums2))

