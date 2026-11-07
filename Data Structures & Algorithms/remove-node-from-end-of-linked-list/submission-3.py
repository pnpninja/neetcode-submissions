# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        counter = 0
        end = head
        while counter < n and end is not None:
            counter+=1
            end = end.next
        if counter == 1 and end is None:
            return None
        if counter == n and end is None:
            return head.next
        prev, start = None, head
        while end is not None:
            prev = start
            start = start.next
            end = end.next
        prev.next = start.next
        return head