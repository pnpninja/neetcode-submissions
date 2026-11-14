# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None or head.next is None:
            return head
        newHead = self.reverseList(head.next)
        head.next.next = head
        head.next = None
        return newHead

    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if head is None:
            return head
        iter, l, prev = head, 0, None
        while iter is not None and l < k:
            prev = iter
            iter = iter.next
            l+=1
        if l < k:
            return head
        # Reverse
        prev.next = None
        next = self.reverseKGroup(iter, k)
        newHead = self.reverseList(head)
        head.next = next
        return newHead
