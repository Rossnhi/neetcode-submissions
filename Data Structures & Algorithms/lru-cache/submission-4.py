class Node:
    def __init__(self, key = None, val = 0, next = None, prev = None):
        self.key = key
        self.val = val
        self.next = next
        self.prev = prev

class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.store = {}
        self.head = Node()
        self.tail = Node()
        self.head.next = self.tail
        self.tail.prev = self.head

    def get(self, key: int) -> int:
        if key in self.store:
            node = self.store[key]
            node.prev.next = node.next
            node.next.prev = node.prev
            node.next = self.tail
            node.prev = self.tail.prev
            self.tail.prev.next = node
            self.tail.prev = node
            return node.val
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.store:
            node = self.store[key]
            self.get(key)
            node.val = value
        else:
            node = Node(key, value, self.tail, self.tail.prev)
            self.tail.prev.next = node
            self.tail.prev = node
            self.store[key] = node
        while len(self.store) > self.capacity:
            node = self.head.next
            self.head.next = node.next
            node.next.prev = self.head
            node.prev = None
            node.next = None
            self.store.pop(node.key)