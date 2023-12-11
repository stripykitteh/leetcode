from typing import List

class SnakeGame:

    def __init__(self, width: int, height: int, food: List[List[int]]):
        self.width = width
        self.height = height
        self.snake_pos = [[0,0]]        
        self.food = food
        self.score = 0
        self.just_eaten = False

    def move(self, direction: str) -> int:
        '''
        look at whether the move is possible (does not touch the snake or the
        walls)
        this includes removing the tail cell (if appropriate) before inserting
        the head cell
        if the move is impossible, return -1
        else
          insert the new head
          check if we just ate
          if we did, increment the score and remove the head of the food list
          return the score
        '''

        # take a copy of the head just in case the snake is only 1 cell long
        head_copy = self.snake_pos[0]
        
        # delete the tail of the snake if necessary and update the just_eaten
        # flag
        if self.just_eaten == True:
            self.just_eaten = False
        else:
            del self.snake_pos[-1]

        # is the move possible?
        if direction == "L":
            new_head = [head_copy[0], head_copy[1]-1]
        elif direction == "R":
            new_head = [head_copy[0], head_copy[1]+1]
        elif direction == "U":
            new_head = [head_copy[0]-1, head_copy[1]]
        else:
            new_head = [head_copy[0]+1, head_copy[1]]

        if SnakeGame.is_legal(new_head, self.snake_pos, self.width, self.height) == False:
            return -1
        
        # insert the new cell
        self.snake_pos.insert(0, new_head)

        # check if we reached the food, if we did update the score and the food
        # list (if there's no food left then skip the check)
        if self.food:
            if (new_head == self.food[0]):
                self.score += 1
                del self.food[0]
                self.just_eaten = True
            
        return self.score
    
    def is_legal(new_head: List[int], snake: List[List[int]], width, height) -> bool:
        # check if we are outside the walls
        if new_head[0] < 0 or new_head[0] >= height or new_head[1] < 0 or new_head[1] >= width:
            return False
        # check if we collided with ourselves
        if new_head in snake:
            return False
        else:
            return True
            

if __name__ == '__main__':

    #function_calls = ["SnakeGame", "move", "move", "move", "move", "move", "move"]
    #parameters = [[3, 2, [[1, 2], [0, 1]]], ["R"], ["D"], ["R"], ["U"], ["L"], ["U"]]

    obj = SnakeGame(2,2, [[0,1]])
    param_1 = obj.move("R")
    param_2 = obj.move("D")



 
