# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        dummy = curr = ListNode()
        while True:
            min = -1
            for i in range(len(lists)):
                if lists[i]:
                    if min == -1 or lists[min].val > lists[i].val:
                        min = i
            if min == -1:
                break
            else:
                curr.next = lists[min]
                curr = lists[min]
                lists[min] = curr.next
        return dummy.next