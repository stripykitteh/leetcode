from math import sqrt

from typing import List

class Solution:

    def areaOfMaxDiagonal(self, dimensions: List[List[int]]) -> int:                    

        best = 0
        for i in range(len(dimensions)):
            diagonal = sqrt(dimensions[i][0]**2 + dimensions[i][1]**2)
            if diagonal > sqrt(dimensions[best][0]**2 + dimensions[best][1]**2):
                best = i
            elif diagonal == sqrt(dimensions[best][0]**2 + dimensions[best][1]**2):
                if dimensions[i][0] * dimensions[i][1] > dimensions[best][0] * dimensions[best][1]:
                    best = i

        return dimensions[best][0] * dimensions[best][1]

if __name__ == '__main__':

    dimensions = [[9,3],[8,6]]
    print(Solution().areaOfMaxDiagonal(dimensions))
    dimensions = [[3,4],[4,3]]
    print(Solution().areaOfMaxDiagonal(dimensions))
    dimensions = [[3,4],[4,3],[4,10],[9,5],[3,11]]
    print(Solution().areaOfMaxDiagonal(dimensions))


        
