from typing import List
from operator import itemgetter

class Solution:

    def orangesRotting(self, grid: List[List[int]]) -> int:

        rotten,fresh = [],[]

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    fresh.append((i,j))
                elif grid[i][j] == 2:
                    rotten.append((i,j))

        ret_val = 0
        while fresh:
            newly_rotten = []
            for i in fresh:
                neighbours = [(i[0]-1,i[1]), (i[0]+1,i[1]), (i[0],i[1]-1), (i[0],i[1]+1)]
                if any([j for j in rotten if j in neighbours]):
                    newly_rotten.append(i)
            if newly_rotten:
                ret_val += 1
                fresh = [k for k in fresh if k not in newly_rotten]
                rotten.extend(newly_rotten)
            else:
                return -1
            #print(rotten,fresh,newly_rotten,ret_val)

        return ret_val
            
if __name__ == '__main__':

    grid = [[2,1,1],[1,1,0],[0,1,1]]
    print(Solution().orangesRotting(grid))    
    grid = [[2,1,1],[0,1,1],[1,0,1]]
    print(Solution().orangesRotting(grid))    
    grid = [[0,2]]    
    print(Solution().orangesRotting(grid))

