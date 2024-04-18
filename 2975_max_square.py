from typing import List

class Solution:
    
    def maximizeSquareArea(self, m: int, n: int, hFences: List[int], vFences: List[int]) -> int:

        modulo = 10**9 + 7

        hFences.insert(0,1)
        hFences.append(m)        
        vFences.insert(0,1)
        vFences.append(n)

        hFences = sorted(hFences)
        vFences = sorted(vFences)
        
        hLengths = set()
        vLengths = set()
        
        for i in range(len(hFences)-1):
            for j in range(i+1,len(hFences)):
                hLengths.add(hFences[j]-hFences[i])
        hLengths = sorted(hLengths,reverse=True)
        
        for i in range(len(vFences)-1):
            for j in range(i+1,len(vFences)):
                vLengths.add(vFences[j]-vFences[i])
        vLengths = sorted(vLengths,reverse=True)

        print(hFences,vFences)
        print(hLengths,vLengths)
        for i in hLengths:
            if i in vLengths:
                return i**2 % modulo

        return -1

        
if __name__ == '__main__':

    m,n,hFences, vFences = 4,3,[2,3],[2]
    print(Solution().maximizeSquareArea(m,n,hFences,vFences))
    m,n,hFences, vFences = 6,7,[2],[4]
    print(Solution().maximizeSquareArea(m,n,hFences,vFences))    
    m,n,hFences, vFences = 3,9,[2],[8,6,5,4]
    print(Solution().maximizeSquareArea(m,n,hFences,vFences))    

