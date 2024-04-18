from typing import List

class Solution:

    def maxArea(self, height: List[int]) -> int:

        d = {}
        l_h = len(height)
        for i in range(l_h):
            d[i] = {}
            d[i]["l"] = height[i]*(l_h - i - 1)
            d[i]["r"] = height[i]*i

        print(sorted(d.items(), key=Solution.get_left, reverse=True))
        print(sorted(d.items(), key=Solution.get_right, reverse=True))

        return 0

    def get_left(item):
        l = item[1]["l"]
        return l

    def get_right(item):
        r = item[1]["r"]
        return r

if __name__ == '__main__':

    height = [1,8,6,2,5,4,8,3,7]
    print(Solution().maxArea(height))
    height = [1,1]
    print(Solution().maxArea(height))
