# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        # find length
        n = 0
        curr = head
        while curr != None:
            n += 1
            if curr.next == None:
                tail = curr
            curr = curr.next
        if n == 1:
            return
        half = math.ceil(n / 2)

        # find the middle element
        n = 0
        curr = head
        prev = None
        while n < half:
            n += 1
            prev = curr
            curr = curr.next
        prev.next = None # cur the list after prev 
        
        # second list starts at curr - reverse it
        next = curr.next
        curr.next = None
        while next != None:
            temp = next.next
            next.next = curr
            curr = next
            next = temp
        
        # merge the two lists
        left = head
        right = curr
        while left or right:
            temp1 = left.next if left else None
            temp2 = right.next if right else None
            if left:
                left.next = right
            if right:
                right.next = temp1
            left = temp1
            right = temp2
