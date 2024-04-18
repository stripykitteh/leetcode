import numpy as np

from typing import List

class Solution:
    
    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:

        missing = 0
        duplicate = 0
        
        item = list(range(1,(len(grid[0])+1)**2))

        # print(item)
        
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] in item:
                    item.remove(grid[i][j])
                else:
                    duplicate = grid[i][j]

        # print(missing)
        missing = item[0]

        return ([duplicate, missing])
                

if __name__ == '__main__':

    # grid = [[1,3],[2,2]]
    grid = [[9,1,7],[8,9,2],[3,4,6]]
    
    print(Solution().findMissingAndRepeatedValues(grid))



        
