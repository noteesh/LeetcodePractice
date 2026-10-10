class Solution:
    def minEatingSpeed(self, piles: list[int], h: int) -> int:
        piles.sort()
        if h == len(piles):
            return piles[-1]
        
        l = 1
        r = piles[-1]
        ret = -1
        while l <= r:
            m = (l + r) //2

            temp = self.eatingSpeed(piles, m)

            if temp <= h:
                r = m - 1
                ret = m
            else:
                l = m + 1

        return ret

    def eatingSpeed(self, piles, k):
        h = 0
        for n in piles:
            h += (-(n // -k))
        return h        


        