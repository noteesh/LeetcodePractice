class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap = points
        
        for i, n in enumerate(points):
            x = n[0]
            y = n[1]

            eucDistance = math.sqrt(math.pow(x - 0, 2) + math.pow(y - 0, 2))
            heap[i] = (eucDistance * -1, x, y)
        
        heapq.heapify(heap)
        
        while len(heap) > k:
            heapq.heappop(heap)
        
        ret = []
        for n in heap:
            print(n[0])
            ret.append([n[1], n[2]])
        
        return ret
        
        



        