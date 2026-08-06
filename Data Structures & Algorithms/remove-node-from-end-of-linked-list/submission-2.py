# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        total_length = 0
        fast = head
        slow = head
        if(head==None or head.next==None):
            return None
        for i in range(0,n):
            fast=fast.next
        prev_slow =None
        while(fast):
            fast=fast.next
            prev_slow=slow
            slow=slow.next
        if(prev_slow==None):
            return head.next
        if(prev_slow.next.next==None):
            prev_slow.next=None
            return head
        prev_slow.next = prev_slow.next.next
        return head