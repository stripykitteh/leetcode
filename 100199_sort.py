from typing import List

class Solution:

    def canSortArray(self, nums: List[int]) -> bool:    

        s = sorted(nums)

        n_c = list(map(Solution.countSetBits, nums))
        s_c = list(map(Solution.countSetBits, s))        

        #print(n_c)
        #print(s_c)

        if n_c != s_c:
            return False

        c = 0
        for i in range(1,len(n_c)):
            if n_c[i-1] == n_c[i]:
                c += 1
            else:
                if max(nums[i - c - 1:i]) > nums[i]:
                    return False
                else:
                    c = 0

        return True
    

    def countSetBits(n: int) -> int:
        count = 0
        while (n):
            count += n & 1
            n >>= 1
        return count

if __name__ == '__main__':

    nums = [8,4,2,30,15]    
    print(Solution().canSortArray(nums))
    nums = [1,2,3,4,5]    
    print(Solution().canSortArray(nums))
    nums = [3,16,8,4,2]
    print(Solution().canSortArray(nums))
    nums = [75,34,30]
    print(Solution().canSortArray(nums))


    
