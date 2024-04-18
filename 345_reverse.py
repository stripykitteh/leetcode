from typing import List

class Solution:

    def reverseVowels(self, s: str) -> str:

        local_s = list(s)
        
        vowels = {'a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'}
        vowel_idx = []
        
        for i in range(len(local_s)):
            if local_s[i] in vowels:
                vowel_idx.append(i)

        for j in range(len(vowel_idx)//2):
            first_vowel = local_s[vowel_idx[j]]
            local_s[vowel_idx[j]] = local_s[vowel_idx[len(vowel_idx) - j - 1]]
            local_s[vowel_idx[len(vowel_idx) - j - 1]] = first_vowel

        return "".join(local_s)
        
if __name__ == '__main__':

    s = "hello"
    print(Solution().reverseVowels(s))
    s = "leetcode"
    print(Solution().reverseVowels(s))
