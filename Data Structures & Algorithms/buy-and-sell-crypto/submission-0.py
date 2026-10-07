class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = float('-inf')
        buy = float('inf')
        for i in range(len(prices)):
            buy = min(prices[i],buy)
            profit = max(profit, prices[i]-buy)

        return 0 if profit == float('-inf') else profit
