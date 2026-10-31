class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        frequencyMap = defaultdict(int)
        minHeap = []
        for num in nums:
            frequencyMap[num]+=1
        for num, freq in frequencyMap.items():
            if len(minHeap) < k:
                heapq.heappush(minHeap, (freq, num))
            else:
                freq_heap_top, freq_heap_top_num = minHeap[0]
                if freq > freq_heap_top:
                    heapq.heappop(minHeap)
                    heapq.heappush(minHeap, (freq, num))
        ans = []
        while minHeap:
            _, num = heapq.heappop(minHeap)
            ans.append(num)
        return ans
