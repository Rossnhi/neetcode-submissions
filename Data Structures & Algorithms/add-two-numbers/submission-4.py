# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        curr1 = l1
        curr2 = l2
        curr = head = ListNode()
        c = 0
        while curr1 != None or curr2 != None:
            c += curr1.val if curr1 else 0
            c += curr2.val if curr2 else 0
            curr.next = ListNode(c % 10)
            c //= 10
            curr = curr.next
            curr1 = curr1.next if curr1 else None
            curr2 = curr2.next if curr2 else None
        if c != 0:
            curr.next = ListNode(c)
        return head.next