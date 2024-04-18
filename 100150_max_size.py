from math import sqrt

from typing import List

class Solution:

    def maximumSetSize(self, nums1: List[int], nums2: List[int]) -> int:

        length = len(nums1)
        my_set = []
        
        # remove as many elements of s1 that appear in s2 and vice-versa
        # iterate over each list
        dict_1 = {x:nums1.count(x) for x in nums1}
        dict_2 = {x:nums2.count(x) for x in nums2}        

        items_1 = 0
        taken_1 = 0
        for key, value in sorted(list(dict_1.items()), key=lambda x:x[1]):
            print (key, value)
            if key not in dict_2:
                my_set.append(key)
                items_1 += 1
                taken_1 += value
            if taken_1 >= length / 2:
                break

        if taken_1 < length / 2:
            for key, value in sorted(list(dict_1.items()), key=lambda x:x[1]):
                print (key, value)
                if key in dict_1:
                    my_set.append(key)                    
                    items_1 += 1
                    taken_1 += value
                if taken_1 >= length / 2:
                    break

        items_2 = 0
        taken_2 = 0
               
        if taken_2 < length / 2:
            for key, value in sorted(list(dict_2.items()), key=lambda x:x[1]):
                print (key, value)
                if key in dict_1:
                    my_set.append(key)
                    items_2 += 1
                    taken_2 += value
                if taken_2 >= length / 2:
                    break

        if taken_2 < length / 2:
            for key, value in sorted(list(dict_2.items()), key=lambda x:x[1]):
                print (key, value)
                if key in dict_2:
                    my_set.append(key)                    
                    items_2 += 1
                    taken_2 += value
                if taken_2 >= length / 2:
                    break
                
        # now we have all distinct items
        print(items_1, taken_1, items_2, taken_2)
        print(my_set)

        return 0

        
if __name__ == '__main__':

    nums1 = [1,2,1,2]
    nums2 = [1,1,1,1]
    print(Solution().maximumSetSize(nums1,nums2))
    nums1 = [1,2,3,4,5,6]
    nums2 = [2,3,2,3,2,3]
    print(Solution().maximumSetSize(nums1,nums2))
    nums1 = [1,1,2,2,3,3]
    nums2 = [4,4,5,5,6,6]
    print(Solution().maximumSetSize(nums1,nums2))



        
