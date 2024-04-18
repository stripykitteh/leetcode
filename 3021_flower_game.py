from typing import List

class Solution:

    def flowerGame(self, n: int, m: int) -> int:
        
        return n * m // 2
    
if __name__ == '__main__':

    n, m = 3, 2
    print(Solution().flowerGame(n,m))    
    n, m = 0, 0
    print(Solution().flowerGame(n,m))    
