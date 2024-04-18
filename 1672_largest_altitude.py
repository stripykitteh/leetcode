from typing import List

class Solution:
    def largestAltitude(self, gain: List[int]) -> int:

        a = 0
        b = 0
        
        for i in range(len(gain)):
            a += gain[i]
            if a > b:
                b = a

        return b
    
if __name__ == '__main__':

    gain = [-5,1,5,0,-7]
    print(Solution().largestAltitude(gain))
    gain = [-4,-3,-2,-1,4,3,2]
    print(Solution().largestAltitude(gain))
    
