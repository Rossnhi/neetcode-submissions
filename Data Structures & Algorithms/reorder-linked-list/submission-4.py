# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        # find middle
        slow = fast = head
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next
        head2 = slow.next
        slow.next = None
        # reverse second half
        prev = None
        curr = head2
        while curr:
            next = curr.next
            curr.next = prev
            prev = curr
            curr = next
        head2 = prev
        # merge both lists
        curr1 = head
        curr2 = head2
        while curr2:
            temp1 = curr1.next
            temp2 = curr2.next
            curr1.next = curr2
            curr2.next = temp1
            curr1 = temp1
            curr2 = temp2
