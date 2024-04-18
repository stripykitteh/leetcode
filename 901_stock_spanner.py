from typing import List

class StockSpanner:

    def __init__(self):
        self.monotone = []

    def next(self, price: int) -> int:

        len_mon = len(self.monotone)
        ret_val = next((i+1 for i,v in enumerate(self.monotone) if v > price), len_mon+1)
        self.monotone.insert(0,price)
        print("monotone=>",self.monotone)        
        return ret_val

if __name__ == '__main__':

    stock_spanner = StockSpanner()
    print(stock_spanner.next(100))
    print(stock_spanner.next(80))
    print(stock_spanner.next(60))
    print(stock_spanner.next(70))
    print(stock_spanner.next(60))
    print(stock_spanner.next(75))
    print(stock_spanner.next(85))


 
