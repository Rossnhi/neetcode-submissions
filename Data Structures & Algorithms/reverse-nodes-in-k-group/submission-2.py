# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        dummy1 = ListNode()
        groupTail = dummy1
        curr = head
        while True:
            start = curr
            check = start
            lessThanK = False
            for i in range(k):
                if check == None:
                    lessThanK = True
                    break
                check = check.next

            if lessThanK:
                groupTail.next = start
                break
            prev = curr
            curr = curr.next
            for i in range(k - 1):
                next = curr.next
                curr.next = prev
                prev = curr
                curr = next
            groupTail.next = prev
            groupTail = start
        return dummy1.next