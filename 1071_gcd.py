from typing import List

class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:

        if str1 + str2 != str2 + str1:
            return ""
        else:
            return str1[0:Solution.gcd(len(str1), len(str2))]

    def gcd(a, b):
        while b:
            a, b = b, a % b
        return a
        
if __name__ == '__main__':

    str1 = "ABCABC"
    str2 = "ABC"
    print(Solution().gcdOfStrings(str1,str2))
    str1 = "ABABAB"
    str2 = "AB"
    print(Solution().gcdOfStrings(str1,str2))
    str1 = "LEET"
    str2 = "CODE"
    print(Solution().gcdOfStrings(str1,str2))


   
