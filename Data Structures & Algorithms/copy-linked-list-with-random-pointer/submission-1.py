"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def __init__(self):
        self.map = defaultdict(Node)

    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if head is None:
            return None
        if head in self.map:
            return self.map[head]
        headCopy = Node(head.val)
        self.map[head] = headCopy
        headCopy.next = self.copyRandomList(head.next)
        headCopy.random = self.copyRandomList(head.random)
        return headCopy