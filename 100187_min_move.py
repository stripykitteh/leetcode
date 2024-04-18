from math import sqrt

from typing import List

class Solution:

    def minMovesToCaptureTheQueen(self, a: int, b: int, c: int, d: int, e: int, f: int) -> int:

        # is rook lined up with queen?
        if a == e:
            if a == c and (b < d < f or b > d > f) :
                return 2
            else:
                return 1
        elif b == f:
            if b == d and (a < c < e or a > c > e):
                return 2
            else:
                return 1
        else:
            rook_moves = 2

        # does bishop have same parity as queen?
        if (c + d) % 2 == (e + f) % 2:
            if c + d == e + f:
                if a + b == c + d and (c < a < e or c > a > e):
                    return 2
                else:
                    return 1
            elif c - d == e - f:
                if a - b == c - d and (c < a < e or c > a > e):
                    return 2
                else:
                    return 1
            else:
                return rook_moves
        else:
            return rook_moves
        
if __name__ == '__main__':

    a = 8
    b = 4
    c = 7
    d = 5
    e = 5
    f = 5
    print(Solution().minMovesToCaptureTheQueen(a,b,c,d,e,f))    



        
