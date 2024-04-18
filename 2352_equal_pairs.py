from typing import List

class Solution:

    def equalPairs(self, grid: List[List[int]]) -> int:

        pivot = list(map(list, zip(*grid)))

        ret_val = 0
        for i in range(len(grid)):
            ret_val += pivot.count(grid[i])

        return ret_val
            
if __name__ == '__main__':

    grid = [[3,2,1],[1,7,6],[2,7,7]]
    print(Solution().equalPairs(grid))
    grid = [[3,1,2,2],[1,4,4,5],[2,4,2,2],[2,4,2,2]]
    print(Solution().equalPairs(grid))
