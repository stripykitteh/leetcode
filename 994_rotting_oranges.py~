from typing import List
from operator import itemgetter

class Solution:

    def nearestExit(self, maze: List[List[str]], entrance: List[int]) -> int:    

        visited, unvisited = {}, {tuple(entrance):0}

        # look at the adjacent cells and see if we can move
        while unvisited:
            cell = (k := next(iter(unvisited)), unvisited.pop(k))

            # check top
            if cell[0][0] > 0 and maze[cell[0][0]-1][cell[0][1]] == '.':
                if (cell[0][0] == 1 or cell[0][1] == 0 or cell[0][1] == len(maze[0])-1) \
                   and (cell[0][0]-1,cell[0][1]) != tuple(entrance):
                    return cell[1] + 1
                if (cell[0][0]-1,cell[0][1]) not in visited and \
                   (cell[0][0]-1,cell[0][1]) not in unvisited:
                    unvisited[(cell[0][0]-1,cell[0][1])] = cell[1] + 1
            # check bottom
            if cell[0][0] < len(maze)-1 and maze[cell[0][0]+1][cell[0][1]] == '.':
                if (cell[0][0] == len(maze)-2 or cell[0][1] == 0 or cell[0][1] == len(maze[0])-1) \
                   and (cell[0][0]+1,cell[0][1]) != tuple(entrance):
                    return cell[1] + 1
                if (cell[0][0]+1,cell[0][1]) not in visited and \
                   (cell[0][0]+1,cell[0][1]) not in unvisited:
                    unvisited[(cell[0][0]+1,cell[0][1])] = cell[1] + 1
            # check left             
            if cell[0][1] > 0 and maze[cell[0][0]][cell[0][1]-1] == '.':
                if (cell[0][0] == 0 or cell[0][0] == len(maze)-1 or cell[0][1] == 1) \
                   and (cell[0][0],cell[0][1]-1) != tuple(entrance):
                    return cell[1] + 1
                if (cell[0][0],cell[0][1]-1) not in visited and \
                   (cell[0][0],cell[0][1]-1) not in unvisited:
                    unvisited[(cell[0][0],cell[0][1]-1)] = cell[1] + 1
            # check right
            if cell[0][1] < len(maze[0])-1 and maze[cell[0][0]][cell[0][1]+1] == '.':
                if (cell[0][0] == 0 or cell[0][0] == len(maze)-1 or cell[0][1] == len(maze[0])-2) \
                   and (cell[0][0],cell[0][1]+1) != tuple(entrance):
                    return cell[1] + 1
                if (cell[0][0],cell[0][1]+1) not in visited and \
                   (cell[0][0],cell[0][1]+1) not in unvisited:
                    unvisited[(cell[0][0],cell[0][1]+1)] = cell[1] + 1

            visited[cell[0]] = cell[1]

            #print("visited=>",visited,"unvisited=>",unvisited,"cell=>",cell)

        return -1
            
if __name__ == '__main__':

    maze,entrance = [["+","+",".","+"],[".",".",".","+"],["+","+","+","."]],[1,2]
    print(Solution().nearestExit(maze,entrance))    
    maze,entrace = [["+","+","+"],[".",".","."],["+","+","+"]],[1,0]
    print(Solution().nearestExit(maze,entrance))    
    maze,entrance = [[".","+"]],[0,0]    
    print(Solution().nearestExit(maze,entrance))
    maze,entrance = [[".","+","+","+","+"],[".","+",".",".","."],[".","+",".","+","."],[".",".",".","+","."],["+","+","+","+","."]],[0,0]    
    print(Solution().nearestExit(maze,entrance))
    maze,entrance = [["+",".","+","+","+","+","+"],["+",".","+",".",".",".","+"],["+",".","+",".","+",".","+"],["+",".",".",".","+",".","+"],["+","+","+","+","+",".","+"]],[0,1]
    print(Solution().nearestExit(maze,entrance))
    maze,entrance = [["+","+","+","+"],["+",".",".","+"],["+",".",".","+"],["+",".",".","+"],["+","+","+","+"]],[1,2]    
    print(Solution().nearestExit(maze,entrance))
    maze,entrance=[["+",".","+","+","+","+","+"],["+",".","+",".",".",".","+"],["+",".","+",".","+",".","+"],["+",".",".",".","+",".","+"],["+","+","+","+","+",".","+"]],[0,1]
    print(Solution().nearestExit(maze,entrance))    

