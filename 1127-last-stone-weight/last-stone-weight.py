class Solution:
    def lastStoneWeight(self, stones: list[int]) -> int:
        heap = []
        heapq.heapify(heap)

        for n in stones:
            heapq.heappush(heap, -1 * n)
        
        while len(heap) > 1:
            s1 = heapq.heappop(heap)
            s2 = heapq.heappop(heap)
            temp = abs(s1 - s2)
            if temp > 0:
                heapq.heappush(heap, -1 * temp)
        
        if len(heap) == 0:
            return 0
        return -1 * heap[0]