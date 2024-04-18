from typing import List

class Solution:

    def beautifulIndices(self, s: str, a: str, b: str, k: int) -> List[int]:

        ret_val = []
        a_index = []
        b_index = []
        
        index = 0
        while index < len(s):
            index = s.find(a, index)
            if index == -1:
                break
            else:
                a_index.append(index)
                index += 1

        index = 0
        while index < len(s):
            index = s.find(b, index)
            if index == -1:
                break
            else:
                b_index.append(index)
                index += 1

        #print(a_index, b_index)

        for i in a_index:
            if next((x for x in b_index if abs(i - x) <= k), None) is not None:
                ret_val.append(i)

        return ret_val
        
    
if __name__ == '__main__':

    s, a, b, k = "isawsquirrelnearmysquirrelhouseohmy", "my", "squirrel", 15
    print(Solution().beautifulIndices(s,a,b,k))
    s, a, b, k = "abcd", "a", "a", 4
    print(Solution().beautifulIndices(s,a,b,k))    
    s, a, b, k = "isawsquirrelnearmysquirrelhouseohmy", "my", "squirrel", 14
    print(Solution().beautifulIndices(s,a,b,k))

