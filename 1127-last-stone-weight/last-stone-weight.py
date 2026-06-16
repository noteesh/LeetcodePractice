class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:

        for i, n in enumerate(stones):
            stones[i] = n * -1

        heap = stones
        heapq.heapify(heap)

        while len(stones) > 1:
            y = heapq.heappop(heap)
            x = heapq.heappop(heap)


            if y == x:
                continue
            else:
                heapq.heappush(heap, y - x)

        if not stones:
            return 0
        return -1 * stones[0]
        