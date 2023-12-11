from typing import List

class Logger:
    delay = 10

    def __init__(self):
        self.messages = {}

    def shouldPrintMessage(self, timestamp: int, message: str) -> bool:
        '''
        look at the timestamp and message
        if message doesn't exist in messages dict, add it, update the timestamp and
        return True
        if it does exist, check if we can print it (check timestamp against next
        allowed)
        if yes then update the timestamp and return True, if not just return False
        '''
        #print(self.messages)
        if message in self.messages:
            if self.messages[message] > timestamp:
                return False

        self.messages[message] = timestamp + self.delay

        return True
            

if __name__ == '__main__':

    # ["Logger", "shouldPrintMessage", "shouldPrintMessage", "shouldPrintMessage", "shouldPrintMessage", "shouldPrintMessage", "shouldPrintMessage"]
    # [[], [1, "foo"], [2, "bar"], [3, "foo"], [8, "bar"], [10, "foo"], [11, "foo"]]    

    obj = Logger()
    param_1 = obj.shouldPrintMessage(1, "foo")
    param_2 = obj.shouldPrintMessage(2, "bar")
    param_3 = obj.shouldPrintMessage(3, "foo")
    param_4 = obj.shouldPrintMessage(8, "bar")
    param_5 = obj.shouldPrintMessage(10, "foo")
    param_6 = obj.shouldPrintMessage(11, "foo")




 
