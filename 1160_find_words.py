from typing import List

class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        # set a counter to zero
        # iterate over list of words
        # check whether the word is "good" by using regexp
        # if it is increment the counter by the length of the word
        # return the counter

        counter = 0
        
        for word in words:
            good = True
            charscopy = chars
            print(counter,word,charscopy)
            for i in range(len(word)):
                if word[i] in charscopy:
                    charscopy=charscopy.replace(word[i],"",1)
                else:
                    good = False
                    break
            if good == True:
                counter += len(word)            

        return counter
    
if __name__ == '__main__':

    words = ["cat","bt","hat","tree"]
    chars = "atach"

    print(Solution().countCharacters(words,chars))
 
