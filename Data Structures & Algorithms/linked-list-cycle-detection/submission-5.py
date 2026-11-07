# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if head == None or head.next == None:
            return False
        slow, fast = head, head.next
        while slow != fast:
            slow = slow.next
            fast = fast.next
            if fast == None or fast.next == None:
                return False
            fast = fast.next
        return True

    # Get start of cycle
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head == None or head.next == None:
            return None
        slow, fast = head, head.next
        while slow != fast:
            slow = slow.next
            fast = fast.next
            if fast == None or fast.next == None:
                return None
            fast = fast.next
        iter = head
        while fast.next != iter:
            fast = fast.next
            iter = iter.next
        return iter