from typing import List

class Solution:

    def maxArea(self, height: List[int]) -> int:

        d = {}
        l_h = len(height)
        
        for i in range(l_h):
            d[i] = height[i]

        d_s = dict(sorted(d.items(), key=lambda item: item[1], reverse=True))
        
        l = l_h - 1
        r = 0
        best = 0
       
        for key in d_s:
            l = min(l, key)
            r = max(r, key)
            best = max(best, (key - l)*d_s[key], (r - key)*d_s[key])
            
        return best
    
if __name__ == '__main__':

    height = [1,8,6,2,5,4,8,3,7]
    print(Solution().maxArea(height))
    height = [1,1]
    print(Solution().maxArea(height))


