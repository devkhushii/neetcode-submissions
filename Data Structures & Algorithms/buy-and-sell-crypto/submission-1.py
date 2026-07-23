class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        if n <= 1:
            return 0
        
        left = 0
        right = left + 1
        max_profit = 0
        while right < n:
            diff = prices[right] - prices[left]
            max_profit = max(max_profit, diff)
            if diff < 0:
                left = right
                right = left +1
                continue
            else:
                right += 1
        return max_profit