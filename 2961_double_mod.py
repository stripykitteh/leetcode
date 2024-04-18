import numpy as np

from typing import List

class Solution:
    def getGoodIndices(self, variables: List[List[int]], target: int) -> List[int]:    

        good = []

        for i in range(len(variables)):
            if target == (variables[i][0]**variables[i][1] % 10)**variables[i][2] % variables[i][3]:
                good.append(i)
                    
        return good

if __name__ == '__main__':

    variables = [[2,3,3,10],[3,3,3,1],[6,1,1,4]]
    target = 2
    print(Solution().getGoodIndices(variables, target))
    variables = [[39,3,1000,1000]]
    target = 17
    print(Solution().getGoodIndices(variables, target))
