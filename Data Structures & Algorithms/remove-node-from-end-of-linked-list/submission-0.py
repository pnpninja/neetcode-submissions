# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        front_ptr = head
        ctr = n
        while front_ptr and ctr > 0:
            front_ptr = front_ptr.next
            ctr-=1
        start, prev_start = head, None
        while front_ptr:
            prev_start = start
            front_ptr = front_ptr.next
            start = start.next
        if prev_start == None:
            return head.next
        prev_start.next = start.next
        return head