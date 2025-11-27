class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        m = max(candies)
        enoughCandies = m - extraCandies
        ret = []

        for i in range(len(candies)):
            if candies[i] < enoughCandies:
                ret.append(False)
            else: 
                ret.append(True)
                
        return ret