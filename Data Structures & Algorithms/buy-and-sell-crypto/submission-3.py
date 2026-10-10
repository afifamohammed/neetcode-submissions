class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        # keep track of the cheaper price
        # maximum profit possible

        buy = prices[0]
        profit = 0

        for i in prices:
            if i < buy:
                buy = i
            profit = max(profit, i - buy)

        return profit


        