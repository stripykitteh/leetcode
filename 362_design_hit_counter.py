from collections import deque

class HitCounter:
    
    hitWindow = 300
    
    def __init__(self):
        self.hitList = deque([])
        
    def hit(self, timestamp: int) -> None:
        self.hitList.append(timestamp)

    def getHits(self, timestamp: int) -> int:
        #print(self.hitList)
        if not self.hitList:
            return 0
        # iterate backwards thru the list
        i = 0
        while self.hitList[-(i+1)] > timestamp - self.hitWindow:
            i += 1
            if i == len(self.hitList):
                break

        # delete the part of the list that's too old
        too_old = len(self.hitList) - i
        for j in range(too_old):
            self.hitList.popleft()
        
        return i

# Your HitCounter object will be instantiated and called as such:
# obj = HitCounter()
# obj.hit(timestamp)
# param_2 = obj.getHits(timestamp)    

if __name__ == '__main__':

    obj = HitCounter()
    print(obj.getHits(100))
    print(obj.getHits(200))
    print(obj.getHits(300))    
    print(obj.hit(300))
    print(obj.hit(401))
    print(obj.getHits(402))



        
