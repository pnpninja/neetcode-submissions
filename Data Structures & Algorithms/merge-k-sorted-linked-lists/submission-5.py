# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        minHeap = []
        for i in range(len(lists)):
            if lists[i] is not None:
                heapq.heappush(minHeap, (lists[i].val, i, lists[i]))
        newHead, iter = None, None
        while minHeap:
            val, i, l = heapq.heappop(minHeap)
            if newHead is None:
                newHead = l
                iter = l
            else:
                iter.next = l
            iter = l
            if l.next is not None:
                heapq.heappush(minHeap, (l.next.val, i, l.next))
        return newHead