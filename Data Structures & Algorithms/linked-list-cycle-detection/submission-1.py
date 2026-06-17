# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        fast = head.next
        slow = head
        if(fast==None):
            return(False)
        while(fast.next!=None or fast!=None):
            if(fast.val==slow.val):
                return(True)
            fast=fast.next
            if(fast==None):
                break
            if(fast.next==None):
                break
            fast=fast.next
            if(fast==None):
                break
            slow = slow.next
        return(False)
        