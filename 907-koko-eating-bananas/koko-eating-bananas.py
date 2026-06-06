class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        piles.sort()

        if h == len(piles):
            return piles[-1]
        elif h < len(piles):
            return -1

        k = 0
        left = 1
        right = piles[-1]
        mid = 0

        while left <= right:
            mid = (left + right) // 2

            curHours = self.eatingSpeed(piles, mid)

            if curHours <= h:
                k = mid
                right = mid - 1
            elif curHours > h:
                left = mid + 1
        return k
    
    def eatingSpeed(self, piles: List[int], k: int) -> int:
        h = 0
        for n in piles:
            h += (-(n // -k))
        return h