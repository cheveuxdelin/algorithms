from __future__ import annotations

class Node:
    def __init__(self, key: int = 0, value: int = 0, previous: Node | None = None, next: Node | None = None) -> None:
        self.key = key
        self.value = value
        self.previous = previous
        self.next = next


class LRUCache:

    def __init__(self, capacity: int):
        self.d: dict[int, Node] = {}
        self.capacity = capacity
        self.left = Node()
        self.right = Node()
        self.left.next = self.right
        self.right.previous = self.left

    def remove(self, node: Node):
        previous = node.previous
        next = node.next
        previous.next = next
        next.previous = previous

    def insert(self, node: Node):
        previous = self.right.previous
        next = self.right
        previous.next = node
        next.previous = node
        node.previous = previous
        node.next = next

    def get(self, key: int) -> int:
        if key not in self.d:
            return -1
        else:
            self.remove(self.d[key])
            self.insert(self.d[key])
            return self.d[key].value

    def put(self, key: int, value: int) -> None:
        if key in self.d:
            self.remove(self.d[key])
        new_node = Node(key, value)
        self.insert(new_node)
        self.d[key] = new_node
        if len(self.d) > self.capacity:
            lru = self.left.next
            self.remove(lru)
            del self.d[lru.key]
