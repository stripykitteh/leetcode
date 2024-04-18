from typing import List
from collections import Counter

class Solution:

    def closeStrings(self, word1: str, word2: str) -> bool:    

        c1, c2 = Counter(word1), Counter(word2)

        if set(c1.keys()) != set(c2.keys()):
            return False

        return (True if sorted(c1.values()) == sorted(c2.values()) else False)
            
if __name__ == '__main__':

    word1 = "abc"
    word2 = "bca"
    print(Solution().closeStrings(word1,word2))
    word1 = "a"
    word2 = "aa"
    print(Solution().closeStrings(word1,word2))    
    word1 = "cabbba"
    word2 = "abbccc"
    print(Solution().closeStrings(word1,word2))    
    word1 = "uau"
    word2 = "ssx"
    print(Solution().closeStrings(word1,word2))    


