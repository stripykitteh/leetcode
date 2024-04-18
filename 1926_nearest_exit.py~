from typing import List
from operator import itemgetter

class Solution:
    
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:

        d = {}

        for i in range(len(equations)):
            if equations[i][0] in d:
                d[equations[i][0]].update({equations[i][1]: values[i]})
            else:
                d[equations[i][0]] = {equations[i][1]: values[i]}
            if equations[i][1] in d:
                d[equations[i][1]].update({equations[i][0]: 1/values[i]})                
            else:
                d[equations[i][1]] = {equations[i][0]: 1/values[i]}                
        
        #print("d=>",d)
        ret_list = []

        for i in queries:
            # test if both numerator and denominator are in d
            if not(i[0] in d and i[1] in d):
                ret_list.append(-1.0)
                continue
            else:
                ret_val = 1.0
            
            # test if numerator and denominator are the same
            if i[0] == i[1]:
                ret_list.append(1.0)
                continue
            
            '''
            Find a path from the numerator to the denominator, return -1.0 if
            no path is found.
            Use 2 queues - a list of processed/unprocessed edges
            '''
            doneList,toDoList = [],[]
            found = False
            for key in d[i[0]]:
                toDoList.append([i[0],key])
            while toDoList:
                curr = toDoList.pop(0)
                if curr[1] == i[1]:
                    doneList.append(curr)
                    found = True
                    break
                else:
                    if curr[1] not in list(map(itemgetter(0), doneList)):                    
                        for key in d[curr[1]]:
                            toDoList.append([curr[1],key])
                    doneList.append(curr)

            if not Found:
                ret_list.append(-1.0)
                continue
            
            '''
            doneList now contains an in-order list of the edges that go from the
            numerator to the denominator. It may contain other edges but we know
            the second element of the last node is the denominator.
            '''
            #print("done=>",doneList,"toDo=>",toDoList,"curr=>",curr)

            doneList.reverse()
            sources = list(map(itemgetter(0), doneList))
            destinations = list(map(itemgetter(1), doneList))
            #print("sources>",sources,"destinations=>",destinations)
            
            curr_idx = 0
            while True:
                ret_val *= d[sources[curr_idx]][destinations[curr_idx]]
                if sources[curr_idx] == i[0]:
                    break
                curr_idx = destinations[curr_idx:].index(sources[curr_idx]) + curr_idx
                
            ret_list.append(ret_val)
            
        return ret_list
            

if __name__ == '__main__':

    equations, values, queries = [["a","b"],["b","c"]],[2.0,3.0],[["a","c"],["b","a"],["a","e"],["a","a"],["x","x"]]
    print(Solution().calcEquation(equations,values,queries))
    equations, values, queries = [["a","b"],["b","c"],["bc","cd"]],[1.5,2.5,5.0],[["a","c"],["c","b"],["bc","cd"],["cd","bc"]]
    print(Solution().calcEquation(equations,values,queries))
    equations, values, queries = [["a","b"]],[0.5],[["a","b"],["b","a"],["a","c"],["x","y"]]
    print(Solution().calcEquation(equations,values,queries))
    equations, values, queries = [["x1","x2"],["x2","x3"],["x3","x4"],["x4","x5"]],[3.0,4.0,5.0,6.0],[["x1","x5"],["x5","x2"],["x2","x4"],["x2","x2"],["x2","x9"],["x9","x9"]]    
    print(Solution().calcEquation(equations,values,queries))
    

