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
        if head is None:
            return head
        # Create a copy
        iter = head
        while iter is not None:
            iterCopy = Node(iter.val)
            iterCopy.next = iter.next
            iter.next = iterCopy
            iter = iterCopy.next
        # Now, make the random connections
        iter = head
        while iter is not None:
            if iter.random:
                iter.next.random = iter.random.next
            iter = iter.next.next
        # Now, disconnect the copy
        iter, iterCopy = head, head.next
        while iter is not None:
            iter2 = iter.next
            iter.next = iter2.next
            if iter2.next:
                iter2.next = iter2.next.next
            iter = iter.next
        return iterCopy