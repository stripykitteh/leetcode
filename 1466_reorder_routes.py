from typing import List

class Solution:

    def minReorder(self, n: int, connections: List[List[int]]) -> int:

        d = {}

        for i in connections:
            if i[0] in d:
                d[i[0]][1].append(i[1])
            else:
                d[i[0]] = [[],[i[1]]]
            if i[1] in d:
                d[i[1]][0].append(i[0])
            else:
                d[i[1]] = [[i[0]],[]]
        
        #print("d=>",d)
        ends = [k for k, v in d.items() if len(v[0]) + len(v[1]) == 1]
        swaps = 0

        # iterate from one end of the network to zero or until we reach a
        # junction, repeat for all ends
        for i in ends:
            curr = i
            while curr != 0 and len(d[curr][0]) + len(d[curr][1]) < 2:
                if d[curr][0]:
                    tmp = d[curr][1]
                    d[curr][1] = d[curr][0]
                    d[curr][0] = tmp
                    swaps += 1
                    next = d[curr][1][0]
                    d[next][1].remove(curr)
                else:
                    next = d[curr][1][0]
                    d[next][0].remove(curr)
                curr = next
            
        return swaps

if __name__ == '__main__':

    n,connections = 6,[[0,1],[1,3],[2,3],[4,0],[4,5]]
    print(Solution().minReorder(n,connections))
    n,connections = 5,[[1,0],[1,2],[3,2],[3,4]]
    print(Solution().minReorder(n,connections))
    n,connections = 3,[[1,0],[2,0]]    
    print(Solution().minReorder(n,connections))
    n,connections = 6,[[0,2],[0,3],[4,1],[4,5],[5,0]]    
    print(Solution().minReorder(n,connections))
    n,connections = 5,[[1,0],[1,2],[2,3],[4,2]]
    print(Solution().minReorder(n,connections))    
    

