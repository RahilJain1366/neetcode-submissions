class ListNode:

    def __init__(self, key, value):
        self.key = key
        self.val = value
        self.next = None
        self.prev = None

class LRUCache:

    def __init__(self, capacity: int):
        
        self.capacity = capacity
        self.head = ListNode(-1,-1)
        self.tail = ListNode(-1,-1)
        self.head.next = self.tail
        self.tail.prev = self.head
        self.hashmap = {}
        
    def get(self, key: int) -> int:
        
        if key not in self.hashmap:
            return -1
        
        node = self.hashmap[key]
        self.remove(node)
        self.add(node)

        return node.val

    def put(self, key: int, value: int) -> None:

        if key in self.hashmap:
            node_to_delete = self.hashmap[key]
            self.remove(node_to_delete)
            del self.hashmap[node_to_delete.key]
        
        node = ListNode(key, value)
        self.add(node)
        self.hashmap[key] = node

        if self.capacity < len(self.hashmap):
            first_node = self.head.next
            self.remove(first_node)
            del self.hashmap[first_node.key]

    def add(self, node):

        prev_end = self.tail.prev
        prev_end.next = node
        node.next = self.tail
        self.tail.prev = node
        node.prev = prev_end

    def remove(self, node):

        node.next.prev = node.prev
        node.prev.next = node.next
        
