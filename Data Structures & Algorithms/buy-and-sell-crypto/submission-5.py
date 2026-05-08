class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        maxToRight = [0] * len(prices)
        for i in range(-1, -len(prices) - 1, -1):
            if i == -1:
                maxToRight[i] = prices[i]
            else:
                maxToRight[i] = max(prices[i], maxToRight[i + 1])
            profit = max(profit, maxToRight[i] - prices[i])
        return profit