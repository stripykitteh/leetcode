from typing import List

class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:

        '''
        add sanity check at the start to see if we have enough letters
        '''
        board_letters = ''
        word_letters = word
        for row in board:
            board_letters += ''.join(row)

        for i in range(len(word_letters)):
            if word_letters[i] in board_letters:
                board_letters=board_letters.replace(word[i],"",1)
            else:
                return False
                break
          
        '''
        maintain a list of possible sub-strings
        add all cells that match the first letter to the list
        while the list is not empty
        * look at all possible adjacent cells (check they have not been visited for this sub-string before)
        * for each match
          * update the list
        * if there are no matches remove the substring from the list
        if we get to the end of the word and have matched everything, return true
        if our list of possibilities becomes empty, return false
        '''

        # check how many times the first and last characters appear in the word
        first_count = word.count(word[0])
        last_count = word.count(word[-1])
        # if the first character is more common, reverse the string
        if first_count > last_count:
            word = word[::-1]

        ret_val = False
        poss_solutions = []
        # iterate over the grid
        for row in range(len(board)):
            row_str = ''.join(board[row])
            indexes = [x for x, v in enumerate(row_str) if v == word[0]]
            for index in indexes:
                poss_solutions.append([[row,index]])
 
        while poss_solutions != []:
            letter_ptr = len(poss_solutions[0])
            if letter_ptr < len(word):
                # look at last letter, see what adjacent cells exist
                [x,y] = poss_solutions[0][-1]
                # consider left
                if y > 0:
                    if (board[x][y-1] == word[letter_ptr]) and ([x,y-1] not in poss_solutions[0]):
                        new_poss_solution = poss_solutions[0][:]
                        new_poss_solution.append([x,y-1])
                        poss_solutions.append(new_poss_solution)
                # consider right
                if y < len(board[x])-1:
                    if (board[x][y+1] == word[letter_ptr]) and ([x,y+1] not in poss_solutions[0]):
                        new_poss_solution = poss_solutions[0][:]
                        new_poss_solution.append([x,y+1])
                        poss_solutions.append(new_poss_solution)
                # consider above
                if x > 0:
                    if (board[x-1][y] == word[letter_ptr]) and ([x-1,y] not in poss_solutions[0]):
                        new_poss_solution = poss_solutions[0][:]
                        new_poss_solution.append([x-1,y])
                        poss_solutions.append(new_poss_solution)
                # consider below
                if x < len(board)-1:
                    if (board[x+1][y] == word[letter_ptr]) and ([x+1,y] not in poss_solutions[0]):
                        new_poss_solution = poss_solutions[0][:]
                        new_poss_solution.append([x+1,y])
                        poss_solutions.append(new_poss_solution)
                # now go back and eliminate this solution
                del poss_solutions[0]
            else:
                ret_val = True
                break
            
        return ret_val


if __name__ == '__main__':

    #board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]]
    #word = "ABCCED"

    #board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]]
    #word = "ABCB"

    board = [["A","A","A","A","A","A"],["A","A","A","A","A","A"],["A","A","A","A","A","A"],["A","A","A","A","A","A"],["A","A","A","A","A","B"],["A","A","A","A","B","A"]]
    word = "AAAAAAAAAAAAABB"
    print(Solution().exist(board,word))
 
