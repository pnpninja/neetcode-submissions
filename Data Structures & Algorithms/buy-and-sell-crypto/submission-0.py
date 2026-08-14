class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) == 1:
            return 0
        ans = 0
        min_so_far = prices[0]
        ptr = 1
        leng = len(prices)
        while ptr < leng:
            ans=max(ans, prices[ptr] - min_so_far)
            min_so_far = min(min_so_far, prices[ptr])
            ptr+=1
        return ans