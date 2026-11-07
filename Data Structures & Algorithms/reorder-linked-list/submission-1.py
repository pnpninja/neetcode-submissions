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
        if head is None:
            return None
        if head.next is None:
            return head
        revList = self.reverseList(head.next)
        head.next.next = head
        head.next = None
        return revList
    
    def mergeList(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if list1 is None:
            return list2
        if list2 is None:
            return list1
        list1_next = list1.next
        list2_next = list2.next
        list1.next = list2
        list2.next = self.mergeList(list1_next, list2_next)
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
    