# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        # find mid
        slow = fast = head
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next
        # cut list nmid
        curr = slow.next
        slow.next = prev = None
        # reverse 2nd list
        while curr:
            next = curr.next
            curr.next = prev
            prev = curr
            curr = next
        head2 = prev
        # merge both lists
        left = head
        right = head2
        while left and right:
            nextLeft = left.next
            nextRight = right.next
            left.next = right
            right.next = nextLeft
            left = nextLeft
            right = nextRight