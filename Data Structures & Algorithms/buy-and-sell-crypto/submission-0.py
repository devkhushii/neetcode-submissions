class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        minPrice=prices[0]
        max_profit=0

        for price in prices:
            minPrice=min(minPrice,price)
            profit=price-minPrice
            max_profit=max(max_profit,profit)

        return max_profit

        