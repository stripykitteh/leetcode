from typing import List
import heapq

class Solution:

    def totalCost(self, costs: List[int], k: int, candidates: int) -> int:

        z = []
        for i,j in enumerate(costs):
            z.append([j,i])

        z.sort(key=lambda x:(x[1],x[0]))

        heap = []
        
        front_ptr = min(candidates-1,len(costs)-1)
        back_ptr = max(front_ptr+1,len(costs)-candidates)
        
        for i in range(front_ptr+1):
            heapq.heappush(heap,z[i])
        
        for i in range(back_ptr,len(costs)):
            heapq.heappush(heap,z[i])

        total_cost = 0
        for i in range(k):
            hire = heapq.heappop(heap)
            total_cost += hire[0]
            if back_ptr > front_ptr+1 and i<k-1:
                if hire[1] <= front_ptr:
                    front_ptr+=1
                    heapq.heappush(heap,z[front_ptr])
                else:
                    back_ptr-=1
                    heapq.heappush(heap,z[back_ptr])

        return total_cost
    
if __name__ == '__main__':

    costs,k,candidates = [17,12,10,2,7,2,11,20,8],3,4
    print(Solution().totalCost(costs,k,candidates))        
    costs,k,candidates = [1,2,4,1],3,3
    print(Solution().totalCost(costs,k,candidates))    
