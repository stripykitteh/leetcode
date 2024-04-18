import numpy as np

from typing import List

class Solution:
    def maximizeSquareArea(self, m: int, n: int, hFences: List[int], vFences: List[int]) -> int:

        hSizes = []
        vSizes = []

        hFences.append(1)
        hFences.append(m)        
        vFences.append(1)
        vFences.append(n)
        
        hFences.sort()
        vFences.sort()

        #print(hFences, vFences)

        h_length = len(hFences) - 1
        v_length = len(vFences) - 1

        # get all differences in hFences h_length apart
        # get all differences in vFences v_length apart
        # decrement h_length and v_length
        # look at whether the h and v differences overlap at all

        length_counts = {}
        
        while True:
            if h_length > 0:
                for i in range(h_length, len(hFences)):
                    this_length = hFences[i] - hFences[i - h_length]
                    if this_length not in length_counts:
                        length_counts[this_length] = [1,0]
                    else:
                        length_counts[this_length][0] += 1
                h_length -= 1

            if v_length > 0:
                for i in range(v_length, len(vFences)):
                    this_length = vFences[i] - vFences[i - v_length]                
                    if this_length not in length_counts:
                        length_counts[this_length] = [0,1]
                    else:
                        length_counts[this_length][1] += 1
                v_length -= 1
            
            #print(h_length, v_length)
            #for i in reversed(sorted(length_counts)):
                #print(i, length_counts[i])
            
            if h_length == 0 and v_length == 0:
                for i in reversed(sorted(length_counts)):
                    if length_counts[i][0] > 0 and length_counts[i][1] > 0:
                        return i**2 % 1000000007
                return -1


if __name__ == '__main__':

    m = 8
    n = 6
    hFences = [4]
    vFences = [5,2,3]
    print(Solution().maximizeSquareArea(m,n,hFences,vFences))
