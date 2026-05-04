# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        dummy1 = ListNode()
        dummy2 = dummy1
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
                dummy2.next = start
                break
            prev = curr
            curr = curr.next
            for i in range(k - 1):
                next = curr.next if curr else None
                curr.next = prev
                prev = curr
                curr = next
            dummy2.next = prev
            dummy2 = start
        return dummy1.next