# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        n1 = 0
        digit = 1
        curr = l1
        while curr != None:
            n1 += digit * curr.val
            digit *= 10
            curr = curr.next
        n2 = 0
        digit = 1
        curr = l2
        while curr != None:
            n2 += digit * curr.val
            digit *= 10
            curr = curr.next
        n = n1 + n2
        head = ListNode(n % 10)
        n //= 10
        curr = head
        while n > 0:
            curr.next = ListNode(n % 10)
            curr = curr.next
            n //= 10
        return head