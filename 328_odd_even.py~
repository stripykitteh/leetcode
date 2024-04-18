from typing import List, Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:

        # two pointer approach:
        # fast pointer moves 2 steps every iteration
        # slow pointer moves 1 step every iteration
        # when the fast pointer reaches the end, the slow pointer is at the
        # node we want to remove
        
        dummy = ListNode(0,head)
        fast, slow = dummy, dummy

        if not fast.next.next:
            return None

        while fast.next and fast.next.next:
            fast = fast.next.next
            slow = slow.next

        print(slow.val,fast.val)
        middle = slow.next
        slow.next = middle.next
        
        return head

if __name__ == '__main__':

    #obj3 = ListNode(3,None)
    #obj2 = ListNode(2,obj3)
    obj1 = ListNode(1,None)
    print(Solution().deleteMiddle(obj1))

