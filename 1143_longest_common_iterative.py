from typing import List

class Solution:    

    def longestCommonSubsequence(self, text1: str, text2: str, acc: int=0) -> int:
        
        set1 = set(text1)
        set2 = set(text2)
        common = set1.intersection(set2)
        if not common:
            return 0
        set1_drop = ''.join(list(set1.difference(common)))
        text1_table = str.maketrans("X","X",set1_drop)
        text1_drop = text1.translate(text1_table)
        set2_drop = ''.join(list(set2.difference(common)))
        text2_table = str.maketrans("X","X",set2_drop)
        text2_drop = text2.translate(text2_table)

        # by convention make text1 the shorter string
        if len(text1_drop) > len(text2_drop):
            tmp = text2_drop
            text2_drop = text1_drop
            text1_drop = tmp

        #print(text1_drop,text2_drop)

        # main iteration step
        matches = {(-1,): 0}
        for text2_ptr in range(len(text2_drop)):
            new_matches = {}
            for key in matches:
                # find all of the matches
                #print("length=>",len(text1_drop[key[-1]+1:]))
                old_k = float('-inf')
                for k in [j for j in range(len(text1_drop[key[-1]+1:])) \
                          if text1_drop[key[-1]+1:][j] == text2_drop[text2_ptr]]:
                    # ignore consecutive runs of the same character
                    if k == old_k+1:
                        continue
                    #print("text2_drop[text2_ptr]=>",text2_drop[text2_ptr],"key=>",key,"k=>",k)
                    new_matches[key+(key[-1]+k+1,)] = matches[key]+1
                    #print("new_matches=>",new_matches)
                    old_k = k
            matches |= new_matches
            #print("matches=>",matches)
                    
        return max(matches.values())
        
if __name__ == '__main__':

    text1,text2 = "abcde","ace"
    print(Solution().longestCommonSubsequence(text1,text2))
    text1,text2 = "abc","abc"
    print(Solution().longestCommonSubsequence(text1,text2))
    text1,text2 = "abc","def"
    print(Solution().longestCommonSubsequence(text1,text2))    
    text1,text2 ="oxcpqrsvwf","shmtulqrypy"
    print(Solution().longestCommonSubsequence(text1,text2))
    text1,text2 ="abcde","aabbccddee"
    print(Solution().longestCommonSubsequence(text1,text2))
    text1,text2 = "aaaaaaaaaaaaaaaaaaaaa","aaaaaaaaaaaaaaaaaaaaa"
    print(Solution().longestCommonSubsequence(text1,text2))    
