from typing import List

class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        '''
        add sanity check at the start to see if we have enough letters
        now we split the board into even and odd cells
        and check even and odd starting points separately
        '''

        even_board_letters_orig = ''
        odd_board_letters_orig = ''
        even_word_letters = word[0::2]
        odd_word_letters = word[1::2]
         
        for row in range(len(board)):
            if row % 2 == 0:
                even_board_letters_orig += ''.join(board[row][0::2])
                odd_board_letters_orig += ''.join(board[row][1::2])
            else:
                even_board_letters_orig += ''.join(board[row][1::2])
                odd_board_letters_orig += ''.join(board[row][0::2])

        even_board_letters = even_board_letters_orig
        odd_board_letters = odd_board_letters_orig        
            
        # starting on an even board position
        even_even_good = True
        even_odd_good = True
        even_possible = False
        
        for i in range(len(even_word_letters)):
            if even_word_letters[i] in even_board_letters:
                even_board_letters=even_board_letters.replace(even_word_letters[i],"",1)
            else:
                even_even_good = False
                break

        for i in range(len(odd_word_letters)):
            if odd_word_letters[i] in odd_board_letters:
                odd_board_letters=odd_board_letters.replace(odd_word_letters[i],"",1)
            else:
                even_odd_good = False
                break

        if even_even_good == True and even_odd_good == True:
            even_possible = True

        # starting on an odd board position
        # need to reset the board letters for the second run
        even_board_letters = even_board_letters_orig
        odd_board_letters = odd_board_letters_orig        

        odd_even_good = True
        odd_odd_good = True
        odd_possible = False
        
        for i in range(len(even_word_letters)):
            if even_word_letters[i] in odd_board_letters:
                odd_board_letters=odd_board_letters.replace(even_word_letters[i],"",1)
            else:
                odd_even_good = False
                break

        for i in range(len(odd_word_letters)):
            if odd_word_letters[i] in even_board_letters:
                even_board_letters=even_board_letters.replace(odd_word_letters[i],"",1)
            else:
                odd_odd_good = False
                break

        if odd_even_good == True and odd_odd_good == True:
            odd_possible = True

        # if neither an even or odd starting cell is possible we quit
        if even_possible == False and odd_possible == False:
            return False

        '''
        maintain a list of possible sub-strings
        add all cells that match the first letter to the list
        while the list is not empty
        * look at the sub-string at the front of the list
        * look at all possible adjacent cells (check they have not been visited
          for this sub-string before)
        * for each match
          * insert a new, longer sub-string behind the current sub-string (DFS)
        * remove the substring from the list
        if we get to the end of the word and have matched everything, return true
        if our list of possibilities becomes empty, return false
        '''
        
        ret_val = False
        poss_solutions = []
        # iterate over the grid
        for row in range(len(board)):
            row_str = ''.join(board[row])
            indexes = [x for x, v in enumerate(row_str) if v == word[0]]
            for index in indexes:
                # check if this is a valid starting point
                if (row + index) % 2 == 0 and even_possible:
                    poss_solutions.append([[row,index]])
                if (row + index) % 2 == 1 and odd_possible:
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
                        poss_solutions.insert(1,new_poss_solution)
                # consider right
                if y < len(board[x])-1:
                    if (board[x][y+1] == word[letter_ptr]) and ([x,y+1] not in poss_solutions[0]):
                        new_poss_solution = poss_solutions[0][:]
                        new_poss_solution.append([x,y+1])
                        poss_solutions.insert(1,new_poss_solution)
                # consider above
                if x > 0:
                    if (board[x-1][y] == word[letter_ptr]) and ([x-1,y] not in poss_solutions[0]):
                        new_poss_solution = poss_solutions[0][:]
                        new_poss_solution.append([x-1,y])
                        poss_solutions.insert(1,new_poss_solution)
                # consider below
                if x < len(board)-1:
                    if (board[x+1][y] == word[letter_ptr]) and ([x+1,y] not in poss_solutions[0]):
                        new_poss_solution = poss_solutions[0][:]
                        new_poss_solution.append([x+1,y])
                        poss_solutions.insert(1,new_poss_solution)
                # now go back and eliminate this solution
                del poss_solutions[0]
            else:
                ret_val = True
                break

        return ret_val


if __name__ == '__main__':

    board = [["a","a","b","a","a","b"],["b","a","b","a","b","b"],["b","a","b","b","b","b"],["a","a","b","a","b","a"],["b","b","a","a","a","b"],["b","b","b","a","b","a"]]
    word = "aaaababab"
    print(Solution().exist(board,word))
 
