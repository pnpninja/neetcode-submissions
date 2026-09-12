class MedianFinder:

    def __init__(self):
        self.bottom_half = [] # max heap
        self.top_half = [] # min heap
    def addNum(self, num: int) -> None:
        heapq.heappush(self.bottom_half, -num)
        if len(self.top_half) > 0:
            heapq.heappush(self.bottom_half, -heapq.heappop(self.top_half))
        while len(self.bottom_half) > len(self.top_half):
            heapq.heappush(self.top_half, -heapq.heappop(self.bottom_half))

    def findMedian(self) -> float:
        if len(self.bottom_half) > len(self.top_half):
            return -self.bottom_half[0]
        elif len(self.bottom_half) < len(self.top_half):
            return self.top_half[0]
        return (self.top_half[0] - self.bottom_half[0])/2