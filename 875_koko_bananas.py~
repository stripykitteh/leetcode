from typing import List
from math import ceil

class Solution:

    def successfulPairs(self, spells: List[int], potions: List[int], success: int) -> List[int]:

        # put spells in a dict with indexes
        d_s = {}
        for i,j in enumerate(spells):
            if j not in d_s:
                d_s[j] = [0]
        r_s_d_s = dict(sorted(d_s.items(),reverse=True))
        
        # sort potions (original order is not important) then put in a dict with
        # indexes
        s_p = sorted(potions)
        d_p = {}
        for i,j in enumerate(s_p):
            if j not in d_p:
                d_p[j] = i

        d_p_k = list(d_p.keys())
        
        # iterate through spells and calculate how many spell*potion combos will
        # be successful

        low = 0        
        for key in r_s_d_s:
            high = len(d_p) - 1        
            guess = -1
            target = ceil(success/key)
            
            # find the values in d_p_k that 'surround' the target
            while True:
                old_guess = guess
                guess = (low+high)//2
                if old_guess == guess:
                    if d_p_k[guess] >= target:
                        r_s_d_s[key] = len(potions) - d_p[d_p_k[guess]]
                    elif d_p_k[guess+1] >= target:
                        r_s_d_s[key] = len(potions) - d_p[d_p_k[guess+1]]                        
                    else:
                        r_s_d_s[key] = 0
                    break 
                if d_p_k[guess] > target:
                    high = guess
                elif d_p_k[guess] == target:
                    r_s_d_s[key] = len(potions) - d_p[d_p_k[guess]]
                    break
                else:
                    low = guess
                #print(key,r_s_d_s,d_p,d_p_k,old_guess,low,guess,high)


        ret_val = [0]*len(spells)
        
        for i in range(len(ret_val)):
            ret_val[i] = r_s_d_s[spells[i]]
            
        return ret_val
        
if __name__ == '__main__':

    spells,potions,success = [5,1,3],[1,2,3,4,5],7
    print(Solution().successfulPairs(spells,potions,success))
    spells,potions,success = [3,1,2],[8,5,8],16
    print(Solution().successfulPairs(spells,potions,success))    
    spells,potions,success = [15,8,19],[38,36,23],328
    print(Solution().successfulPairs(spells,potions,success))    
