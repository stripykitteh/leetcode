from typing import List

mod = 10 ** 9 + 7
class Solution:
    def maximizeSquareArea(self, m: int, n: int, hFences: List[int], vFences: List[int]) -> int:
        a = [1] + hFences + [m]
        b = [1] + vFences + [n]
        a.sort()
        b.sort()
        tmp = set()
        for i in range(len(a)):
            for j in range(i):
                tmp.add(a[i] - a[j])
        print(a,b,tmp)
        ans = -1
        for i in range(len(b)):
            for j in range(i):
                if b[i] - b[j] in tmp:
                    ans = max(ans, (b[i] - b[j]) * (b[i] - b[j]))
        return -1 if ans == -1 else ans % mod

if __name__ == '__main__':

    m = 8
    n = 6
    hFences = [4]
    vFences = [5,2,3]
    print(Solution().maximizeSquareArea(m,n,hFences,vFences))
    
