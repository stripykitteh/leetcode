from typing import List

class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:

        ret_val = ""
        
        for i in range(max(len(word1),len(word2))):
            if i < len(word1):
                ret_val += word1[i]
            if i < len(word2):
                ret_val += word2[i]

        return ret_val

if __name__ == '__main__':

    word1 = "abc"
    word2 = "pqr"
    print(Solution().mergeAlternately(word1,word2))
    word1 = "ab"
    word2 = "pqrs"
    print(Solution().mergeAlternately(word1,word2))
    word1 = "abcd"
    word2 = "pq"
    print(Solution().mergeAlternately(word1,word2))

   
