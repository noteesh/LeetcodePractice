class Solution:
    def kClosest(self, points: list[list[int]], k: int) -> list[list[int]]:
        heap = []
        ret = []

        for x, y in points:
            eucDis = math.sqrt((math.pow((x - 0), 2)) + (math.pow((y - 0), 2)))
            heap.append([eucDis, x, y])
        
        heapq.heapify(heap)

        for i in range(k):
            d, xc, yc = heapq.heappop(heap)
            ret.append([xc, yc])

        return ret