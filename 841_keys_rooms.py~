from typing import List, Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:    
        
        prev = None
        cur = head

        while cur.next:
            cur.next, prev, cur = prev, cur, cur.next

        return prev
                        
    def printNodeList(self, head: Optional[ListNode]) -> None:

        dummy = head

        while True:
            print(dummy.val,end='')
            if dummy.next:
                dummy = dummy.next
            else:
                print()
                break
        
if __name__ == '__main__':

    obj5 = ListNode(5,None)
    obj4 = ListNode(4,obj5)    
    obj3 = ListNode(3,obj4)
    obj2 = ListNode(2,obj3)
    obj1 = ListNode(1,obj2)
    print(Solution().reverseList(obj1))

    obj12 = ListNode(2,None)
    obj11 = ListNode(1,obj12)    
    print(Solution().reverseList(obj11))
    

