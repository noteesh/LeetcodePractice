class Solution:
    def reorganizeString(self, s: str) -> str:
        counter = Counter(s)
            
        heap = []
        for k, v in counter.items():
            heapq.heappush(heap, (-1 * v, k))

        if -1 * heap[0][0] > (len(s) + 1) // 2:
            return ""
        
        ret = ""
        while heap:
            count1, char1 = heapq.heappop(heap)  # most frequent
            
            if not heap:  # only one character left
                if -count1 > 1:  # more than one remaining → impossible
                    return ""
                ret += char1
                break
            
            count2, char2 = heapq.heappop(heap)  # second most frequent
            
            ret += char1 + char2
            
            if count1 + 1 < 0:  # still has remaining count
                heapq.heappush(heap, (count1 + 1, char1))
            if count2 + 1 < 0:
                heapq.heappush(heap, (count2 + 1, char2))

        return ret

        