# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if list1 == None:
            return list2
        if list2 == None:
            return list1
        next1 = list1
        next2 = list2
        if list1.val < list2.val:
            newNode = list1
            next1 = next1.next
        else:
            newNode = list2
            next2 = next2.next
        head = newNode
        while next1 != None and next2 != None:
            if next1.val < next2.val:
                newNode.next = next1
                newNode = next1
                next1 = next1.next
            else:
                newNode.next = next2
                newNode = next2
                next2 = next2.next
        if next1 != None:
            newNode.next = next1
        if next2 != None:
            newNode.next = next2
        return head

