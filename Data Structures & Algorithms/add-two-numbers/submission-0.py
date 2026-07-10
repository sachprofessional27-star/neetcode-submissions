# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        head = ListNode()
        temp = ListNode()
        temp = head
        carry = 0
        check = 0
        while l1 and l2:
            ans = l1.val+l2.val+carry
            if(ans>=10):
                carry = 1
                ans = ans-10
            else:
                carry = 0
            if(check==0):
                temp.val = ans
                check = 1
            else:
                node = ListNode()
                node.val = ans
                temp.next = node
                temp = temp.next
            l1 = l1.next
            l2 = l2.next
        while l1:
            ans = l1.val+carry
            if(ans>=10):
                carry = 1
                ans = ans-10
            else:
                carry = 0
            node = ListNode()
            node.val = ans
            temp.next = node
            temp = temp.next
            l1 = l1.next
        while l2:
            ans = l2.val+carry
            if(ans>=10):
                carry = 1
                ans = ans-10
            else:
                carry = 0
            node = ListNode()
            node.val = ans
            temp.next = node
            temp = temp.next
            l2 = l2.next
        if(carry==1):
            node = ListNode()
            node.val = 1
            temp.next = node
        return head

        