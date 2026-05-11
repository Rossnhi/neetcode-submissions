class Node:
    def __init__(self, val = 0, key = None, next = None) -> None:
        self.val = val 
        self.key = key
        self.next = next
        self.prev = None

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
            node = Node(value, key)
            node.next = self.tail
            node.prev = self.tail.prev
            self.tail.prev.next = node
            self.tail.prev = node
            self.store[key] = node

        while len(self.store) > self.capacity:
            node = self.head.next
            self.store.pop(node.key)
            self.head.next = node.next
            node.next.prev = self.head
            node.next = None
            node.prev = None
