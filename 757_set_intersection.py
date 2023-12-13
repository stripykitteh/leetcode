from typing import List

class Solution:

    def intersectionSizeTwo(self, intervals: List[List[int]]) -> int:
        '''
        sort the intervals by starting value/ending value
        iterate thru intervals left to right
        create "interval targets" where there are overlaps

        i.e., if we have [1,3][3,7][8,9]

        we create this:
        int_src
        -------
        (1,3): 2
        (3,7): 2 (the 2s mean we need to include 2 members of each set)
        (8,9): 2
        
        int_trg
        -------
        (1,2): 1
        (3): 2 (this means we have 2 intervals overlapping)
        (4,7): 1
        (8,9): 1
        '''
        
        int_src = {}
        int_trg = {}
        for interval in sorted(intervals, key=lambda x: (x[0], x[1])):
            print(interval)
            int_src[(interval[0], interval[1])] = 2
            # just insert first element
            if not int_trg:
                int_trg[(interval[0], interval[1])] = 1
            else:
                # iterate backwards from the end of the int_trg dict
                # create/update intervals as required
                if int_trg[-1]interval[1] > int_max:
                    int_trg[(interval[0], interval[1])] = 1
        print(int_src)
        print(int_trg)
        
        return 0
    
if __name__ == '__main__':

    print(Solution().intersectionSizeTwo([[1,3],[3,7],[8,9]]))





 
