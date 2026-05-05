# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        length = 0
        curr = head
        while curr:
            length += 1
            curr = curr.next
        
        m = length - n
        i = 0
        dummy = curr = ListNode(0, head)
        while i < m:
            i += 1
            curr = curr.next

        remNode = curr.next
        curr.next = curr.next.next
        remNode.next = None
        return dummy.next