# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def getPrevMiddleOfList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head == None or head.next == None or head.next.next == None:
            return head
        slow_ptr, fast_ptr, prev_slow_ptr = head, head, None
        while not fast_ptr == None:
            prev_slow_ptr = slow_ptr
            slow_ptr, fast_ptr = slow_ptr.next, fast_ptr.next
            if not fast_ptr == None:
                fast_ptr = fast_ptr.next
        return prev_slow_ptr
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head == None or head.next == None:
            return head
        reverseNext = self.reverseList(head.next)
        head.next.next = head
        head.next = None
        return reverseNext
    def alternateList(self, head1: Optional[ListNode], head2: Optional[ListNode]) -> Optional[ListNode]:
        if not head1 and not head2:
            return None
        elif not head1:
            return head2
        elif not head2:
            return head1
        else:
                head1_next = head1.next
                head1.next = head2
                self.alternateList(head2, head1_next)
                return head1
                
    def reorderList(self, head: Optional[ListNode]) -> None:
        if head == None or head.next == None or head.next.next == None:
            return
        # find prev of middle of list
        prev_middle_list = self.getPrevMiddleOfList(head)
        # break link 
        second_half = prev_middle_list.next
        prev_middle_list.next = None
        # reverse second half
        second_half_reversed = self.reverseList(second_half)
        # alternate
        self.alternateList(head, second_half_reversed)