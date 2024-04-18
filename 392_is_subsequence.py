class Solution:
    
    def isSubsequence(self, s: str, t: str) -> bool:
        j = 0
        for i in range(len(s)):
            try:
                j = t.index(s[i],j) + 1
            except ValueError:
                return False
        return True
        
if __name__ == '__main__':

    s,t = "abc","ahbgdc"    
    print(Solution().isSubsequence(s,t))
    s,t = "axc","ahbgdc"
    print(Solution().isSubsequence(s,t))
    s,t = "aaaaaa","bbaaaa"
    print(Solution().isSubsequence(s,t))
