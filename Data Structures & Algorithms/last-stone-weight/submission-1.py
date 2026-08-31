class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        heap = []
        for stone in stones:
            heapq.heappush(heap, (-stone, stone))
        # Hulk smash
        if len(heap) == 1:
            _, stone = heapq.heappop(heap)
            return stone
        while len(heap) > 1:
            _, stone1 = heapq.heappop(heap)
            _, stone2 = heapq.heappop(heap)
            dif = abs(stone1 - stone2)
            if dif != 0:
                heapq.heappush(heap, (-dif, dif))
        if len(heap) == 0:
            return 0
        _, ans = heapq.heappop(heap)
        return ans