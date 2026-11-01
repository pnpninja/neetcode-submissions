class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        minSoFar, maxProfit = math.inf, 0
        for price in prices:
            minSoFar = min(minSoFar, price)
            maxProfit = max(maxProfit, price - minSoFar)
        return maxProfit
