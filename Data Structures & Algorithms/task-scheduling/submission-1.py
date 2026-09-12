class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        # Get count of each task
        countMap = defaultdict(int)
        for task in tasks:
            countMap[task] = countMap.setdefault(task, 0) + 1
        heap = []
        queue = deque()

        # Populate tasks into maxheap
        for task, count in countMap.items():
            heapq.heappush(heap, -count)
        timer = 0
        while len(heap) > 0 or len(queue) > 0:
            timer+=1
            if len(heap) > 0:
                negCount = heapq.heappop(heap)
                negCount+=1
                if negCount != 0:
                    queue.append([negCount, timer+n])
            while len(queue) > 0:
                [nCount, nextTime] = queue[0]
                if nextTime == timer:
                    queue.popleft()
                    heapq.heappush(heap, nCount)
                else:
                    break
        return timer
        
            