from typing import List

class Solution:
    def canMakePalindromeQueries(self, s: str, queries: List[List[int]]) -> List[bool]:

        ret_list = []

        query_count = 0
        
        for query in queries:
            
            # handle seen queries
            query_index = queries.index(query) if query in queries else -1
            #print("query_index=>",query_index)
            if query_index > -1 and query_index < query_count:
                ret_list.append(ret_list[query_index])
                query_count += 1
                continue
            else:
                query_count += 1
            
            ret_val = True

            if s[0:len(s)//2] == reversed(s[len(s)//2:len(s)]):
                ret_list.append(ret_val)
                continue
            
            #print("query=>", query)
            # consider the parts of the string that are invariant and out of scope
            min_reverse = len(s) - query[2] - 1
            max_reverse = len(s) - query[3] - 1
            min_range = min(query[0], max_reverse)
            max_range = max(query[1], min_reverse)
            #print("min_range=>", min_range, "max_range=>", max_range)

            for i in range(0,min_range - 1):
                #print("min range=>", i, s[i], len(s) - 1 - i, s[len(s) - 1 - i])
                if s[i] != s[len(s) - 1 - i]:
                    ret_val = False
                    break

            if ret_val == False:
                ret_list.append(ret_val)                
                continue
            
            for i in range(max_range + 1, len(s)//2):
                #print("max range=>", i, s[i], len(s) - 1 - i, s[len(s) - 1 - i])                
                if s[i] != s[len(s) - 1 - i]:
                    ret_val = False
                    break

            if ret_val == False:
                ret_list.append(ret_val)
                continue
                
            # now consider the section that can be re-arranged
            low_str = s[min_range : max_range + 1]
            high_str = "".join(reversed(s[len(s) - max_range - 1 : len(s) - min_range]))
            free_fixed = {}
            #print("low_str=>",low_str,"high_str=>",high_str)
            
            # if the strings don't contain the same characters, append False
            if sorted(low_str) != sorted(high_str):
                ret_val = False
                ret_list.append(ret_val)                
                continue
            
            # take counts of whether each character is fixed or free in both the
            # low_str and the high_str
            for i in range(min_range, max_range + 1):
                #print("mid_range=>", i, s[i], len(s) - 1 - i , s[len(s) - 1 - i])
                # if the pair of characters matches and at least one of them is
                # fixed then continue
                if (low_str[i - min_range] == high_str[i - min_range]) and ((query[0] > i or query[1] < i) or (query[3] < len(s) - i - 1 or query[2] > len(s) - i - 1)):
                    continue
                # if the pair of characters does not match but both are fixed return False
                if (low_str[i - min_range] != high_str[i - min_range]) and (query[0] > i or query[1] < i) and (query[3] < len(s) - i - 1 or query[2] > len(s) - i - 1):
                    ret_val = False
                    break
                if query[0] <= i and query[1] >= i:
                    if low_str[i - min_range] in free_fixed:
                        free_fixed[low_str[i - min_range]][0] += 1
                    else:
                        free_fixed[low_str[i - min_range]] = [1,0,0,0]
                else:
                    if low_str[i - min_range] in free_fixed:
                        free_fixed[low_str[i - min_range]][1] += 1
                    else:
                        free_fixed[low_str[i - min_range]] = [0,1,0,0]
                if query[3] >= len(s) - i - 1 and query[2] <= len(s) - i - 1:
                    if high_str[i - min_range] in free_fixed:
                        free_fixed[high_str[i - min_range]][2] += 1
                    else:
                        free_fixed[high_str[i - min_range]] = [0,0,1,0]
                else:
                    if high_str[i - min_range] in free_fixed:
                        free_fixed[high_str[i - min_range]][3] += 1
                    else:
                        free_fixed[high_str[i - min_range]] = [0,0,0,1]                    
                #print("free_fixed=>",free_fixed)

            if ret_val == False:
                ret_list.append(ret_val)                
                continue           

            for key in free_fixed:
                #print(key, free_fixed[key])
                if free_fixed[key][1] > free_fixed[key][2] or free_fixed[key][3] > free_fixed[key][0]:
                    ret_val = False
                    break

            ret_list.append(ret_val)
                    
        return ret_list

if __name__ == '__main__':
    s="bb"
    queries=[[0,0,1,1],[0,0,1,1]]
    #print(Solution().canMakePalindromeQueries(s, queries))
