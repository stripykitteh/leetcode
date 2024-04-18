from typing import List
from math import ceil

class Solution:
    
    def minEatingSpeed(self, piles: List[int], h: int) -> int:

        # put piles in a dict, value is number of piles with that many bananas
        d_p = {}
        bananas = 0
        max_pile = 0
        for i in piles:
            bananas += i
            if i > max_pile:
                max_pile = i
            if i not in d_p:
                d_p[i] = 1
            else:
                d_p[i] += 1

        low = 1
        guess = -1
        success = False
        high = max_pile

        while True:
            old_guess = guess
            old_success = success
            guess = (low+high)//2
            print("**",old_guess,low,guess,high)
            if old_guess == guess:
                return guess + (0 if old_success else 1)
            hours = 0
            success = True
            for key in d_p:
                hours += ceil(key/guess)*d_p[key]
                print("****",hours,key,guess,d_p[key])
                if hours > h:
                    success = False
                    break
            if success:
                high = guess
            else:
                low = guess

        
if __name__ == '__main__':

    piles,h = [3,6,7,11],8
    print(Solution().minEatingSpeed(piles,h))
    piles,h = [30,11,23,4,20],5
    print(Solution().minEatingSpeed(piles,h))    
    piles,h = [30,11,23,4,20],6
    print(Solution().minEatingSpeed(piles,h))
    piles,h = [312884470],968709470
    print(Solution().minEatingSpeed(piles,h))
