# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbersRecur(self, l1: Optional[ListNode], l2: Optional[ListNode], carry: int) -> Optional[ListNode]:
        if not l1 and not l2:
            if carry == 0:
                return None
            else:
                new_node = ListNode(carry%10)
                carry = carry//10
                new_node.next = self.addTwoNumbersRecur(l1, l2, carry)
                return new_node
        if l1:
            carry+=l1.val
            l1 = l1.next
        if l2:
            carry+=l2.val
            l2 = l2.next
        new_node = ListNode(carry%10)
        carry = carry // 10
        new_node.next = self.addTwoNumbersRecur(l1, l2, carry)
        return new_node

    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        return self.addTwoNumbersRecur(l1, l2, 0)