from typing import List
import re

class Solution:

    def predictPartyVictory(self, senate: str) -> str:
        
        while True:
            s = senate[0]
            senate = senate[1:]

            if s == 'R':
                if 'D' not in senate:
                    return 'Radiant'
                else:
                    senate = senate.replace('D','',1)
            else:
                if 'R' not in senate:
                    return 'Dire'
                else:
                    senate = senate.replace('R','',1)

            senate += s

if __name__ == '__main__':

    senate = "RD"
    print(Solution().predictPartyVictory(senate))    
    senate = "RDD"    
    print(Solution().predictPartyVictory(senate))
