from typing import List
import heapq
import collections
import math

class Solution:
    def minimumTime(self, n: int, edges: List[List[int]], disappear: List[int]) -> List[int]:

        def dijkstra(graph, start):
            distances = {vertex: float('infinity') for vertex in graph}
            distances[start] = 0
            priority_queue = [(0, start)]
            vis = set()
            while priority_queue:
                current_distance, current_vertex = heapq.heappop(priority_queue)
                if current_vertex in vis:
                    continue
                vis.add(current_vertex)
                for neighbor, weight in graph[current_vertex].items():
                    distance = current_distance + weight
                    if distance < distances[neighbor]:
                        distances[neighbor] = distance
                        heapq.heappush(priority_queue, (distance, neighbor))
                
            return distances
    
        g = collections.defaultdict(dict)

        for u,v,w in edges:
            if disappear[u] <= w and disappear[v] <= w:
                continue
            if v in g[u]:
                g[u][v] = min(w,g[u][v])
                g[v][u] = min(w,g[u][v])
            else:
                g[u][v] = w
                g[v][u] = w
        print ("g=>",g)
        
        d = dijkstra(g,0)
        print("d=>",d)

        ret_val = []
        for i in range(n):
            if i in d:
                if math.isinf(d[i]):
                    ret_val.append(-1)
                else:
                    ret_val.append(d[i])
            else:
                ret_val.append(-1)
        
        return ret_val

if __name__ == '__main__':

    n = 50000
    print(Solution().minimumTime(n,edges,disappear))