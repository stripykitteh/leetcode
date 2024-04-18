from typing import List
import re

class Solution:

    def decodeString(self, s: str) -> str:    

        ret_val = ''
        stack = []

        r = 0
        for i, c in enumerate(s):
            if c.isnumeric():
                r = r*10 + int(c)
            elif c == '[':
                stack.append([i,r])
                r = 0
            elif c == ']':
                [pos,rpt] = stack.pop()
                if not stack:
                    ret_val += self.decodeString(s[pos+1:i]) * rpt
            else:
                if not stack:
                    ret_val += c

        return ret_val
    
if __name__ == '__main__':

    s = "3[a]2[bc]"
    print(Solution().decodeString(s))
    s = "3[a2[c]]"
    print(Solution().decodeString(s))    
    s = "2[abc]3[cd]ef"
    print(Solution().decodeString(s))
    s = "3[z]2[2[y]pq4[2[jk]e1[f]]]ef"    
    print(Solution().decodeString(s))
