from typing import List

class Solution:
    def maximumLength(self, s: str) -> int:

        special = {}
        last_diff = 0

        for i in range(1,len(s)):
            if s[i] != s[i-1]:
                if s[i-1] in special:
                    special[s[i-1]].append(i - last_diff)
                else:
                    special[s[i-1]] = [i - last_diff]
                last_diff = i

            if i == len(s)-1:
                if s[i] in special:
                    special[s[i]].append(i - last_diff + 1) 
                else:
                    special[s[i]] = [i - last_diff + 1]

        best = 0
        for key in special:
            counter = 0
            for value in reversed(sorted(special[key])):
                print(key, value)
                if counter == 0:
                    first = value
                    if len(special[key]) == 1:
                        best = max(best, first - 2)
                elif counter == 1:
                    second = value
                    if first > second:
                        best = max(best, first - 2, second)
                    else:
                        best = max(best, second - 1)
                elif counter == 2:
                    third = value
                    best = max(best, third)
                counter += 1

        if best >= 1:
            return best
        else:
            return -1


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
    s = "aaaaaabaaaaaaaabaaaaa"
    print(Solution().maximumLength(s))
    s = "ereerrrererrrererre"
    print(Solution().maximumLength(s))
    s = "jinhhhtttttttefffffjjjjjjjjjfffffjjjjjjjjjqvvvvvvg"
    print(Solution().maximumLength(s))    
