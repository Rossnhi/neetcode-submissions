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
        random = defaultdict(lambda : [])
        dummy = new = Node(0)
        curr = head
        while curr:
            new.next = Node(curr.val)
            if curr in random:
                for node in random[curr]:
                    node.random = new.next
            random[curr.random].append(new.next)
            new = new.next
            curr = curr.next
        new = dummy
        curr = head
        while curr:
            if curr in random:
                for node in random[curr]:
                    node.random = new.next
            random[curr.random].append(new.next)
            new = new.next
            curr = curr.next

        return dummy.next