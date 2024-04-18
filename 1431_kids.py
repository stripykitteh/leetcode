from typing import List

class Solution:

    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:

        ret_val = []
        max_candies = max(candies)
        for i in candies:
            ret_val.append(i + extraCandies >= max_candies)

        return ret_val
        
if __name__ == '__main__':

    candies = [2,3,5,1,3]
    extraCandies = 3    
    print(Solution().kidsWithCandies(candies, extraCandies))
    candies = [4,2,1,1,2]
    extraCandies = 1
    print(Solution().kidsWithCandies(candies, extraCandies))
    candies = [12,1,12]
    extraCandies = 10
    print(Solution().kidsWithCandies(candies, extraCandies))
