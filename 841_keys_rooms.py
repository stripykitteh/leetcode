from typing import List

class Solution:
    
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:

        unprocessed_keys, processed_keys = {0},set()
        
        while unprocessed_keys and \
              len(unprocessed_keys) + len(processed_keys) < len(rooms):

            key = unprocessed_keys.pop()          
            new_keys = set(rooms[key])
            processed_keys.add(key)
            unprocessed_keys.update(new_keys - processed_keys)

            print(processed_keys, unprocessed_keys)
            
        if len(unprocessed_keys) + len(processed_keys) == len(rooms):
            return True
        else:
            return False
            
if __name__ == '__main__':

    rooms = [[1],[2],[3],[]]
    print(Solution().canVisitAllRooms(rooms))
    rooms = [[1,3],[3,0,1],[2],[0]]    
    print(Solution().canVisitAllRooms(rooms))
    rooms = [[4],[3],[],[2,5,7],[1],[],[8,9],[],[],[6]]
    print(Solution().canVisitAllRooms(rooms))
    

