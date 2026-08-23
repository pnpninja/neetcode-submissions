class ListNode:
    def __init__(self, key: int, val: int):
        self.key = key
        self.val = val
        self.next = None
        self.prev = None

class DLL:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cur_size = 0
        self.head = ListNode(-1,-1)
        self.tail = ListNode(-1,-1)
        self.head.next = self.tail
        self.tail.prev = self.head
    
    def insert_at_head(self, node: ListNode):
        node.next = self.head.next
        node.next.prev = node
        node.prev = self.head
        self.head.next = node
        self.cur_size += 1
    
    def remove_from_tail(self) -> Optional[ListNode]:
        if self.cur_size == 0:
            return None
        node = self.tail.prev
        self.remove_element(node)
        return node
    
    def remove_element(self, node: ListNode):
        prev_node, next_node = node.prev, node.next
        prev_node.next = next_node
        next_node.prev = prev_node
        node.next = None
        node.prev = None
        self.cur_size-=1

class LRUCache:

    def __init__(self, capacity: int):
        self.map = {}
        self.dll = DLL(capacity=capacity)

    def get(self, key: int) -> int:
        if key in self.map:
            node = self.map[key]
            self.dll.remove_element(node)
            self.dll.insert_at_head(node)
            return node.val
        else:
            return -1

    def put(self, key: int, value: int) -> None:
        # Check if key exists
        if key in self.map:
            node = self.map[key]
            self.dll.remove_element(node)
            node.val = value
            self.dll.insert_at_head(node)
        else:
            # Check capacity
            if self.dll.cur_size == self.dll.capacity:
                # Get least recently used
                least_recently_used = self.dll.remove_from_tail()
                self.map.pop(least_recently_used.key)
            new_node = ListNode(key=key, val=value)
            self.map[key] = new_node
            self.dll.insert_at_head(new_node)

        
