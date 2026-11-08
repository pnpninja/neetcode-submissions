class Node:
    def __init__(self, key:int = 0, val: int = 0, prev: Optional[Node] = None, next: Optional[Node] = None):
        self.key = key
        self.val = val
        self.next = next
        self.prev = prev

class LinkedList:
    def __init__(self, capacity: int = 0):
        self.head = Node()
        self.tail = Node()
        self.head.next = self.tail
        self.tail.prev = self.head
        self.size = 0
        self.capacity = capacity
    
    def add(self, node: Node) -> None:
        node.next = self.head.next
        node.next.prev = node
        node.prev = self.head
        node.prev.next = node
        self.size+=1

    def remove(self, node: Node) -> None:
        node.prev.next = node.next
        node.next.prev = node.prev
        self.size-=1
    
    def getFirst(self) -> Optional[Node]:
        if self.head.next == self.tail:
            return None
        return self.head.next
    
    def getLast(self) -> Optional[Node]:
        if self.tail.prev == self.head:
            return None
        return self.tail.prev
    
    def getSize(self) -> int:
        return self.size
    
    def hasCapacity(self) -> bool:
        return self.size < self.capacity


class LRUCache:

    def __init__(self, capacity: int):
        self.list = LinkedList(capacity=capacity)
        self.map = defaultdict(Node)

    def get(self, key: int) -> int:
        if key in self.map:
            node = self.map[key]
            self.list.remove(node)
            self.list.add(node)
            return node.val
        return -1
        

    def put(self, key: int, value: int) -> None:
        node = None
        if key in self.map:
            self.map[key].val = value
            node = self.map[key]
            self.list.remove(node)
        else: 
            node = Node(key, value)
            self.map[key] = node
            if not self.list.hasCapacity():
                removeNode = self.list.getLast()
                if removeNode is not None:
                    removeKey = removeNode.key
                    self.map.pop(removeKey)
                    self.list.remove(removeNode)
        self.list.add(node)
        
            

        
