from typing import List

class Solution:

    def countKeyChanges(self, s: str) -> int:

        l = s.lower()

        c = 0
        for i in range(1,len(l)):
            if l[i] != l[i-1]:
                c += 1

        return c
    
if __name__ == '__main__':

    s = "aAbBcC"
    print(Solution().countKeyChanges(s))
    s = "AaAaAaaA"
    print(Solution().countKeyChanges(s))    
    s = "A"
    print(Solution().countKeyChanges(s))    

