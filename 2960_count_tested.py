import numpy as np

from typing import List

class Solution:
    def countTestedDevices(self, batteryPercentages: List[int]) -> int:

        tested = 0
        
        for i in range(len(batteryPercentages)):
            if batteryPercentages[i] > 0:
                tested += 1
                for j in range(i+1,len(batteryPercentages)):
                    batteryPercentages[j] = max(0, batteryPercentages[j] - 1)

            #print(batteryPercentages, tested)
                    
        return tested

if __name__ == '__main__':

    batteryPercentages = [1,1,2,1,3]    
    print(Solution().countTestedDevices(batteryPercentages))
    batteryPercentages = [0,1,2]    
    print(Solution().countTestedDevices(batteryPercentages))
