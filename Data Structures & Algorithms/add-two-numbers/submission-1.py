# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def __init__(self):
        self.carry = 0

    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        if l1 is None and l2 is None:
            if self.carry == 0:
                return None
            else:
                return ListNode(self.carry, None)
        l1_val = l1.val if l1 is not None else 0
        l2_val = l2.val if l2 is not None else 0
        new_val = l1_val + l2_val + self.carry
        self.carry = int(new_val / 10)
        new_node = ListNode(new_val % 10)
        l1_next = l1.next if l1 is not None else None
        l2_next = l2.next if l2 is not None else None
        new_node.next = self.addTwoNumbers(l1_next, l2_next)
        return new_node