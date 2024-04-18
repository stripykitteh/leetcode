from typing import List
from collections import Counter
class Solution:

    def uniqueOccurrences(self, arr: List[int]) -> bool:    

        d = Counter(arr)
        
        return len(d.values()) == len(set(d.values()))

if __name__ == '__main__':

    arr = [1,2,2,1,1,3]
    print(Solution().uniqueOccurrences(arr))
    arr = [1,2]
    print(Solution().uniqueOccurrences(arr))
    arr = [-3,0,1,-3,1,1,1,-3,10,0]    
    print(Solution().uniqueOccurrences(arr))

