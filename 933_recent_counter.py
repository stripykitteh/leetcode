from typing import List

class RecentCounter:

    def __init__(self):
        self.queue = []

    def ping(self, t: int) -> int:

        while self.queue and self.queue[0] < t - 3000:
            self.queue.pop(0)

        self.queue.append(t)

        return len(self.queue)
        
    
if __name__ == '__main__':

    # Your RecentCounter object will be instantiated and called as such:
    # obj = RecentCounter()
    # param_1 = obj.ping(t)

    #["RecentCounter","ping","ping","ping","ping"]
    #[[],[1],[100],[3001],[3002]]

    obj = RecentCounter()
    print(obj.ping(1))
    print(obj.ping(100))
    print(obj.ping(3001))
    print(obj.ping(3002))
    
