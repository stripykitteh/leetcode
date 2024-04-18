from typing import List

class Solution:

    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:

        local_fb = [0] + flowerbed + [0]
        
        for i in range(2,len(local_fb)):
            if local_fb[i-2] == local_fb[i-1] == local_fb[i] == 0:
                local_fb[i-1] = 1
                n -= 1
            if n <= 0:
                return True

        return False
        
if __name__ == '__main__':

    flowerbed, n = [1,0,0,0,1], 1
    print(Solution().canPlaceFlowers(flowerbed, n))
    flowerbed, n = [1,0,0,0,1], 2
    print(Solution().canPlaceFlowers(flowerbed, n))
    flowerbed, n = [0,0,1,0,1], 1
    print(Solution().canPlaceFlowers(flowerbed, n))
    flowerbed, n = [1,0,0,0,1,0,0], 2
    print(Solution().canPlaceFlowers(flowerbed, n))
