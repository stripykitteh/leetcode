from typing import List
from statistics import median

class Solution:
    def maxFrequencyScore(self, nums: List[int], k: int) -> int:

        best = 1
        low_ptr = 0
        high_ptr = 1

        nums.sort()

        print(nums)

        inc_low = False
        while high_ptr < len(nums):
            high_ptr += 1
            if inc_low == True:
                low_ptr += 1
                inc_low = False
            my_median = round(median(nums[low_ptr:high_ptr]))

            sum = 0
            i = low_ptr
            while True:
                print(nums[low_ptr:high_ptr], "median=>",my_median, "best=>",best)
                sum += abs(nums[i] - my_median)
                print("i=>",i,"sum=>",sum)                
                if sum > k:
                    print("sum busted")
                    inc_low = True
                    break
                if i - low_ptr + 1 > best:
                    best = i - low_ptr + 1
                    high_ptr += 1
                    my_median = round(median(nums[low_ptr:high_ptr]))
                    sum = 0
                    for j in range(low_ptr,high_ptr):
                        sum += abs(nums[j] - my_median)
                if i < len(nums) - 1:
                    i += 1
                else:
                    print("range busted")
                    break

        return best   

if __name__ == '__main__':

    nums = [1,2,6,4]
    k = 3
    #nums = [1,4,4,2,4]
    #k = 0
    #nums = [10,19,26,18,27,18]
    #k = 9
    #nums = [15,1,27,4,5,20,5,26,28]
    #k = 38

    #nums = [29,10,26,1,2,2,17,7,5,16,24,27,7,7,26,26,24]
    #k = 3

    #nums = [17,24,10,23,22,15,25,2,13,24,22,25,25,21]
    #k = 52

    #nums = [6,29,3,19,10,6,20,26,1,30,11,25,29,12,29,14,15,16,5]
    #k = 64
    
    print(Solution().maxFrequencyScore(nums, k))
    
