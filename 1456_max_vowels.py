from typing import List

class Solution:

    v = "aeiou"
        
    def maxVowels(self, s: str, k: int) -> int:
        
        s_n = list(map(Solution.mapVowel, s))
        s = sum(s_n[:k])
        b = s

        for i in range(1,len(s_n) - k + 1):
            s = s - s_n[i-1] + s_n[i+k-1]
            if s > b:
                b = s
             
        return b
        
    def mapVowel(c: str) -> str:
        return (1 if c in Solution.v else 0)

if __name__ == '__main__':

    s, k = "abciiidef", 3
    print(Solution().maxVowels(s, k))
    s, k = "aeiou", 2
    print(Solution().maxVowels(s, k))
    s, k = "leetcode", 3
    print(Solution().maxVowels(s, k))
    
