# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head == None:
            return None
        curr = head
        next = head.next
        head.next = None
        while next != None:
            temp = next.next
            next.next = curr
            curr = next
            next = temp
        return curr