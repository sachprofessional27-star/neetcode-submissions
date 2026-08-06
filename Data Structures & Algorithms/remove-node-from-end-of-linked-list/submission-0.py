# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        total_length = 0
        temp = ListNode()
        temp = head
        if(head==None):
            return None
        while(temp):
            total_length+=1
            temp = temp.next
        index_to_be_removed = total_length-n
        if(index_to_be_removed == 0): 
            return head.next
        
        counter = 0
        prev = None
        temp = head
        while(temp):
            prev = temp
            temp = temp.next
            counter+=1
            if(counter==index_to_be_removed):
                if(temp==None):
                    prev.next = None
                else:
                    prev.next = temp.next
                break
        
        return head
        