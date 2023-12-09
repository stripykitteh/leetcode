from typing import List

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        # sort the list alphabetically
        strs.sort()
        # neat trick: compare the first and last strings in the list only
        # whatever common prefix they possess is the answer
        # print(strs[0],strs[-1])
        i = 0
        # Append two different characters to the end of the strings to get the
        # enumerate function to terminate correctly
        for i, (x, y) in enumerate(zip(strs[0]+"a",strs[-1]+"b")):
            # print(i,x,y)
            if x!=y:
                break
        return strs[0][:i]

if __name__ == '__main__':

    #strs = ["flower","flow","flight"]
    strs = ["apple","apple"]

    print(Solution().longestCommonPrefix(strs))
 
