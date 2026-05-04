# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if len(lists) == 1:
            return lists[0]
        if len(lists) == 0:
            return None
        newLists = []
        for i in range(0, len(lists), 2): 
            if i == len(lists) - 1:
                newLists.append(lists[i])
                break
            l1 = lists[i]
            l2 = lists[i + 1]
            dummy = curr = ListNode()
            while l1 and l2:
                if l1.val < l2.val:
                    curr.next = l1
                    l1 = l1.next
                else:
                    curr.next = l2
                    l2 = l2.next
                curr = curr.next
            if l1:
                curr.next = l1
            if l2:
                curr.next = l2
            newLists.append(dummy.next)
        return self.mergeKLists(newLists)