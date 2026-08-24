# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        new_head = self.reverseList(head.next)
        head.next.next = head
        head.next = None
        return new_head
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        ctr = 1
        new_head_prev, new_head = None, head
        while ctr <= k:
            new_head_prev = new_head
            new_head = new_head.next
            ctr+=1
            if not new_head:
                break
        if ctr > k:
            new_head_prev.next = None
            reversed_list = self.reverseList(head)
            reversed_after = self.reverseKGroup(new_head, k)
            head.next = reversed_after
            return reversed_list
        else:
            return head
        