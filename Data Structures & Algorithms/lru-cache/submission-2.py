class DoublyLinkedListNode:
    def __init__(self, key, val = 0, next = None, prev = None) -> None:
        self.key = key
        self.val = val
        self.next = next
        self.prev = prev

class LRUCache:

    def __init__(self, capacity: int):
        self.store = {}
        self.capacity = capacity
        self.head = None
        self.tail = None

    def get(self, key: int) -> int:
        if key in self.store:
            node = self.store[key]
            print(self.store)
            if node == self.tail:
                return node.val
            if node.prev:
                node.prev.next = node.next
            if node.next:
                node.next.prev = node.prev
            if node == self.head:
                self.head = node.next
            self.tail.next = node
            node.prev = self.tail
            node.next = None
            self.tail = node
            return node.val
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.store:
            self.get(key)
            self.store[key].val = value
        else:
            node = DoublyLinkedListNode(key, value)
            self.store[key] = node
            if self.head == None:
                self.head = self.tail = node
            else:
                node.prev = self.tail
                self.tail.next = node
                node.next = None
                self.tail = node

        if len(self.store) > self.capacity:
            del self.store[self.head.key]
            self.head.next.prev = None
            temp = self.head
            self.head = self.head.next
            temp.next = None