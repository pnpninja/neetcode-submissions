# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        heap = []
        for ind, li in enumerate(lists):
            if li:
                heapq.heappush(heap,(li.val, ind, li))
        new_head, iter = None, None
        while heap:
            val, ind, l = heapq.heappop(heap)
            if not new_head:
                new_head = l
                iter = l
            else:
                iter.next = l
                iter = iter.next
            l = l.next
            if l:
                heapq.heappush(heap, (l.val, ind, l))
        return new_head
