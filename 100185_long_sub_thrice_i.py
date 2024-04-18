from typing import List

class Solution:
    def maximumLength(self, s: str) -> int:

        special = {}
        sublen = 0
        
        for i in range(len(s)):
            #print("i=>",i, "substr=>", s[:i+1])
            if i == 0:
                special[s[0]] = 1
                sublen = 1
            else:
                if s[i] == s[i-1]:
                    if sublen == 0:
                        sublen = 2
                    else:
                        sublen += 1
                    for j in range(0,sublen):
                        #print("i=>",i,"j=>",j,"sublen=>",sublen, s[i-j:i+1])
                        if s[i-j:i+1] not in special:
                            special[s[i-j:i+1]] = 1
                        else:
                            special[s[i-j:i+1]] += 1
                else:
                    if s[i] not in special:
                        special[s[i]] = 1
                    else:
                        special[s[i]] += 1
                    sublen = 0
            
            #print(i,sublen,special)

        new_special = {k: v for k, v in special.items() if v >= 3}
        #print(new_special)

        if bool(new_special) == False:
            return -1
        else:
            return max(map(len, new_special))


if __name__ == '__main__':

    s = "aaaa"
    print(Solution().maximumLength(s))
    s = "abcdef"
    print(Solution().maximumLength(s))    
    s = "abcaba"
    print(Solution().maximumLength(s))    
    s = "abcccccdddd"
    print(Solution().maximumLength(s))
    s = "aaa"
    print(Solution().maximumLength(s))    
    s = "aaaaaaaaaaaaaa"
    print(Solution().maximumLength(s))    

