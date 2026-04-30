class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        greatestToRight = [prices[_] for _ in range(len(prices))]
        for i in range(len(prices) - 2, -1, -1):
            greatestToRight[i] = max(greatestToRight[i + 1], prices[i])
        for i in range(len(prices)):
            profit = max(profit, greatestToRight[i] - prices[i])
        return profit