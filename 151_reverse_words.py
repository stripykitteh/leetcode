from typing import List

class Solution:

    def reverseWords(self, s: str) -> str:

        words = s.split()

        ret_val = ''
        for i in words[::-1]:
            ret_val += i + ' '
        
        return ret_val[:-1]
    
if __name__ == '__main__':

    s = "the sky is blue"
    print(Solution().reverseWords(s))
    s = "  hello world  "
    print(Solution().reverseWords(s))    
    s = "a good   example"
    print(Solution().reverseWords(s))    

