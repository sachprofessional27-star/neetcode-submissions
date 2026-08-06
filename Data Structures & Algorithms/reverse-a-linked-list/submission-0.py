# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev_node = None
        curr_node = ListNode()
        next_node = ListNode()
        curr_node = head
        if(curr_node==None):
            return None
        if(curr_node.next==None):
            return curr_node
        next_node = curr_node.next
        while(curr_node!=None):
            curr_node.next = prev_node
            prev_node = curr_node
            curr_node = next_node
            if(curr_node!=None):
                next_node = curr_node.next
            else:
                break
        return prev_node
            
        