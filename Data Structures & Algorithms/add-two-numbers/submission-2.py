# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        n = 0
        curr1 = l1.next
        curr2 = l2.next
        c = 0
        head = ListNode()
        if l1 != None:
            c = l1.val
        if l2 != None:
            c += l2.val
        head.val = c % 10
        c //= 10
        curr = head
        while curr1 != None or curr2 != None:
            if curr1 != None:
                c += curr1.val
                curr1 = curr1.next
            if curr2 != None:
                c += curr2.val
                curr2 = curr2.next
            curr.next = ListNode(c % 10)
            print(c % 10, c // 10)
            curr = curr.next
            c //= 10
        if c != 0:
            curr.next = ListNode(c)
        return head            