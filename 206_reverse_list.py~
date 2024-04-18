from typing import List, Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:    
        
        dummy = ListNode(0,head)
        odd, even = dummy, dummy

        if not odd.next:
            return None
        else:
            odd = odd.next

        if even.next.next:
            even_head = even.next.next
        else:
            even_head = None

        print("even_head=>",end='')
        self.printNodeList(even_head)
            
        parity = 1
        while True:
            if parity%2:
                if even.next.next:
                    even.next = even.next.next
                    even = even.next
                else:
                    even.next = None
                    break
            else:
                if odd.next.next:
                    odd.next = odd.next.next
                    odd = odd.next
                else:
                    odd.next = None
                    break
            parity += 1
            
            print("odd=>",end='')
            self.printNodeList(odd)
            print("even=>",end='')        
            self.printNodeList(even)

            
        odd.next = even_head 

        print("odd=>",end='')
        self.printNodeList(odd)
        print("even=>",end='')
        self.printNodeList(even)
        print("head=>",end='')
        self.printNodeList(head)

        return head
    
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
    print(Solution().oddEvenList(obj1))
    #[2,1,3,5,6,4,7]
    obj17 = ListNode(7,None)
    obj16 = ListNode(4,obj17)    
    obj15 = ListNode(6,obj16)
    obj14 = ListNode(5,obj15)
    obj13 = ListNode(3,obj14)
    obj12 = ListNode(1,obj13)
    obj11 = ListNode(2,obj12)    
    print(Solution().oddEvenList(obj11))
    

