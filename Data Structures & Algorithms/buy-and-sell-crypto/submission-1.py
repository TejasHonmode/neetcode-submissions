class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxp = 0
        minprice = prices[0]

        for sellprice in prices[1:]:
            maxp = max(maxp, (sellprice - minprice))
            minprice = min(minprice, sellprice)
        return maxp