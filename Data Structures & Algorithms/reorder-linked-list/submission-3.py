# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def getMiddlePrev(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head == None:
            return None
        if head.next == None:
            return head
        slow_prev, slow, fast = None, head, head
        while fast is not None and fast.next is not None:
            slow_prev = slow
            slow = slow.next
            fast = fast.next.next
        return slow_prev

    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # Iterative approach
        if head is None or head.next is None:
            return head
        prev, iter = head, head.next
        prev.next = None
        while iter is not None:
            iter_next = iter.next
            iter.next = prev
            prev = iter
            iter = iter_next
        return prev
    
    def mergeList(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        # Iterative approach
        head1, head2 = list1, list2
        flip = False
        while head1 is not None and head2 is not None:
            if not flip:
                head1_next = head1.next
                head1.next = head2
                head1 = head1_next
            else:
                head2_next = head2.next
                head2.next = head1
                head2 = head2_next
            flip = not flip
        return list1

 
    def reorderList(self, head: Optional[ListNode]) -> None:
        # Find middle of list.
        middlePrev = self.getMiddlePrev(head)
        # Split the list
        middle = middlePrev.next
        middlePrev.next = None
        # Reverse the second half
        middleReversed = self.reverseList(middle)
        # Merge it
        head = self.mergeList(head, middleReversed)
    