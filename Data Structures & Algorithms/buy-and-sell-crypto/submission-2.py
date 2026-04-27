class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxToRight = [prices[-1]]
        profit = 0
        for i in range(-2, -len(prices), -1):
            maxToRight.insert(0, max(maxToRight[0], prices[i]))
        for i in range(len(prices) - 1):
            profit = max(profit, maxToRight[i] - prices[i])
        return profit