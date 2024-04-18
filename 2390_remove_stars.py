from typing import List

class Solution:

    def removeStars(self, s: str) -> str:

        stack = []
        for i in s:
            if i == '*':
                stack.pop()
            else:
                stack.append(i)
            
        return ''.join(str(c) for c in stack)
    
if __name__ == '__main__':

    s = "leet**cod*e"
    print(Solution().removeStars(s))
    s = "erase*****"    
    print(Solution().removeStars(s))
