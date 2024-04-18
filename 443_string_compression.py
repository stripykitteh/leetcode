from typing import List

class Solution:

    def compress(self, chars: List[str]) -> int:
        
        i = 0
        while i < len(chars):
            j = i+1
            while j < len(chars) and chars[j] == chars[i]:
                j += 1
            if j > i+1:
                c = j-i
                c_l = [*str(c)]
                chars[i+1:j] = []
                chars[i+1:i+1] = c_l
                i += len(c_l) + 1
            else:
                i += 1
            #print("i=>",i,"j=>",j,"chars=>",chars)
        return(len(chars))
    
if __name__ == '__main__':

    chars = ["a","a","b","b","c","c","c"]
    print(Solution().compress(chars))
    chars = ["a"]
    print(Solution().compress(chars))    
    chars = ["a","b","b","b","b","b","b","b","b","b","b","b","b"]
    print(Solution().compress(chars))
