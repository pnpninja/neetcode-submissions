# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if head == None or head.next == None:
            return False
        slow_ptr, fast_ptr = head, head.next
        while not fast_ptr == None and not (slow_ptr == fast_ptr):
            slow_ptr, fast_ptr = slow_ptr.next, fast_ptr.next
            if not fast_ptr == None:
                fast_ptr = fast_ptr.next
            # if slow_ptr == fast_ptr:
            #     return True
        return slow_ptr == fast_ptr