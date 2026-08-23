"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:

    def copyRandomList(self, head: Optional[Node]) -> Optional[Node]:
        # Create a copy right next to it 
        if not head:
            return None
        iter = head
        while iter:
            iter2 = Node(iter.val)
            iter2.next = iter.next
            iter.next = iter2
            iter = iter2.next
        new_head = head.next
        # Copy random pointer
        iter = head
        while iter:
            if iter.random:
                iter.next.random = iter.random.next
            iter = iter.next.next
        # Disconnect copy from old pointers
        iter = head
        while iter:
            iter2 = iter.next
            iter.next = iter2.next
            if iter2.next:
                iter2.next = iter2.next.next
            iter = iter.next
        return new_head


