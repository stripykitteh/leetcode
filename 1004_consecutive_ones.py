from typing import List

class Solution:

    def longestOnes(self, nums: List[int], k: int) -> int:
        # set up dict with lists of 0s and 1s seen
        d = {0:[],1:[]}
        last = 0
        curr = nums[0]

        # by convention the list always starts with a 1
        if curr == 0:
            d[1].append([0,0])

        z_c = 0
        for i in range(1,len(nums)):
            if nums[i] != nums[i-1]:
                d[curr].append([last,i-last])
                if curr == 0:
                    z_c += i-last
                curr, last = nums[i], i

        d[curr].append([last,len(nums)-last])

        # by convention the list always ends with a 1
        if curr == 0:
            d[1].append([len(nums)-1,0])
            z_c += len(nums)-last

        #print(d)
        
        if z_c <= k:
            return len(nums)

        # set up l and r pointers, notation is [partition_number, offset]
        s = 0
        l = [s,0]
        r = [0,0]
        w = k
        while w > 0:
            if d[0][s][1] >= w:
                r = [s, w]
                w = 0
            else:
                w -= d[0][s][1]
                s += 1

            #print("s=>",s,"w=>",w)

        #print(l,r)

        # work out the longest consecutive run of 1s given the current l and r
        # pointers and maintain a best variable

        # set up initial sum when l pointer is at the beginning of the first
        # run of 0s
        sum = k
        best = 0
        for i in range(r[0]+1):
            sum += d[1][i][1]
        if r[1] == d[0][r[0]][1]:
            sum += d[1][r[0]+1][1]

        best = sum
        #print("sum=>",sum,"best=>",best)
            
        # move the l and r pointers rightwards and update the sum
        while True:
            l = Solution.next(l,d)
            r = Solution.next(r,d)
            #print("l=>",l,"r=>",r)
            if r == [-1,0]:
                break
            # check if we need to drop the 1s partition to the left
            if l[1] == 1:
                sum -= d[1][l[0]][1]
                #print("left dropped", d[1][l[0]])
            # check if we need to add the 1s partition to the right
            if r[1] == d[0][r[0]][1]:
                sum += d[1][r[0]+1][1]
                #print("right added", d[1][r[0]+1])
            if sum > best:
                best = sum
            #print("sum=>", sum)
        
        return best

    # given a pointer, return the next position or [-1,0] if EOL
    def next(curr_ptr: List[int], d: List[int]) -> List[int]:

        if d[0][curr_ptr[0]][1] > curr_ptr[1]:
            ret_val = [curr_ptr[0],curr_ptr[1]+1]
        else:
            if len(d[0]) > curr_ptr[0]+1:
                ret_val = [curr_ptr[0]+1,1]
            else:
                ret_val = [-1,0]
        return ret_val
    
if __name__ == '__main__':

    nums, k = [1,1,1,0,0,0,1,1,1,1,0],2
    print(Solution().longestOnes(nums,k))
    nums, k = [0,0,1,1,0,0,1,1,1,0,1,1,0,0,0,1,1,1,1],3
    print(Solution().longestOnes(nums,k))    
    nums, k = [0,0,0,1],3
    print(Solution().longestOnes(nums,k))
    nums, k = [1,0,0,0,1,1,0,0,1,1,0,0,0,0,0,0,1,1,1,1,0,1,0,1,1,1,1,1,1,0,1,0,1,0,0,1,1,0,1,1],8
    print(Solution().longestOnes(nums,k))
    nums, k = [0],1
    print(Solution().longestOnes(nums,k))    
