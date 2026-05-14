# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        length = 0
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            length += 2
        if fast:
            length += 1
        m = length - n
        i = 0
        curr = dummy = ListNode(0, head)
        while i < m:
            i += 1
            curr = curr.next
        curr.next = curr.next.next
        return dummy.next