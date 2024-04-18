from typing import List
import numpy

class Solution:

    def findMaximumNumber(self, k: int, x: int) -> int:

        '''
        asssume x == 1 for now
        for 0..2**n-1, the number of bits set is n * 2**(n-1)
        e.g., if n = 5, the range is 0..31 and the bits set is 5 * 2**4 = 80
        let's start by working out between which values of n k is in
        '''

        n = 1
        while True:
            print(n * 2**(n-1), k)
            if n * 2**(n-1) > k:
                n -= 1
                break
            else:
                n += 1

        print("n=>", n)

        return 0
    
if __name__ == '__main__':

    k, x = 9, 1
    print(Solution().findMaximumNumber(k,x))
    k, x = 7, 2
    print(Solution().findMaximumNumber(k,x))
    k, x = 31, 3
    print(Solution().findMaximumNumber(k,x))
    k, x = 3278539330613, 5    
    print(Solution().findMaximumNumber(k,x))

