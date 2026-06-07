class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        p1 = 0
        p2 = 1
        curMax = 0

        while p2 <= len(prices) - 1:
            if prices[p2] <= prices[p1]:
                p1 = p2
                p2 += 1
                continue
            elif prices[p2] > prices[p1]:
                if prices[p2] - prices[p1] > curMax:
                    curMax = prices[p2] - prices[p1]
            
            p2 += 1
            print(curMax)
        
        return curMax
            
        