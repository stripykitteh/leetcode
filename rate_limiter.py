from typing import List

class RateLimiter:

    def __init__(self, max_requests: int, time_window: int):
        self.customers = {}
        self.max_requests = max_requests
        self.time_window = time_window

    def insert_request(self, customer: str, timestamp: int) -> bool:
        if customer not in self.customers:
            self.customers[customer] = [timestamp]
        else:
            print(len(self.customers[customer]))
            if len(self.customers[customer]) < self.max_requests:
                   self.customers[customer].append(timestamp)
            else:
                   if self.customers[customer][-self.max_requests] >= timestamp - self.time_window:
                       return False
                   else:
                       self.customers[customer].append(timestamp)                       

        print(customer, self.customers[customer])                       
        return True

if __name__ == '__main__':

    
    obj = RateLimiter(5,10)
    
    for i in range(1,100,1):
        if (i % 2):
            print(obj.insert_request("jim", i))
        else:
            print(obj.insert_request("jane", i))        
