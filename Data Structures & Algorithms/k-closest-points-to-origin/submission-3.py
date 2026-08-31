class Solution:
    def getEuclideanDistance(self, x1: int, x2: int, y1: int, y2: int) -> float:
        return math.sqrt(((x2-x1)*(x2-x1))+ ((y2-y1)*(y2-y1)))

    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap = []
        capacity = 0

        for point in points:
            if capacity < k:
                heapq.heappush(heap,(-self.getEuclideanDistance(0,point[0],0,point[1]), point))
                capacity+=1
            else:
                negDistance, _ = heap[0]
                distance = -negDistance
                distance2 = self.getEuclideanDistance(0,point[0],0,point[1])
                if distance2 < distance:
                    heapq.heappop(heap)
                    heapq.heappush(heap,(-distance2, point))
        heapq.heapify(heap)
        ans = []
        while len(heap) > 0:
            _, point = heapq.heappop(heap)
            ans.append(point)
        return ans
                

