class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy_price = prices[0]
        most_profit = 0
        for pr in prices[1:]:
            if pr<buy_price:
                buy_price = pr
            most_profit = max(most_profit, pr-buy_price)
        return most_profit
