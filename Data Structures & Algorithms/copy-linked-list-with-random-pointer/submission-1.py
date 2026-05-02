"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if head is None:
            return None
        randDict = {}
        curr = head
        cHead = copy = Node(0)
        n = 0
        while curr != None:
            print(randDict, curr)
            copy.val = curr.val
            if curr.random:
                if curr.random in randDict:
                    randDict[curr.random].append(copy)
                else:
                    randDict[curr.random] = [copy]
            if curr in randDict:
                for n in randDict[curr]:
                    n.random = copy
            curr = curr.next
            if curr:
                copy.next = Node(0)
                copy = copy.next
        curr = head
        copy = cHead
        while curr != None:
            if curr.random:
                if curr.random in randDict:
                    randDict[curr.random].append(copy)
                else:
                    randDict[curr.random] = [copy]
            if curr in randDict:
                for n in randDict[curr]:
                    n.random = copy
            curr = curr.next
            copy = copy.next
        return cHead