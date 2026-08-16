class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        heap = []
        ans = []
        for ind, num in enumerate(nums):
            heapq.heappush(heap,(-num, ind))
            if len(heap) < k:
                continue
            else:
                while True:
                    max_num, its_index = heap[0]
                    if its_index <= ind - k:
                        heapq.heappop(heap)
                    else:
                        break
                max_num1, its_index1 = heap[0]
                ans.append(-max_num1)
        return ans

