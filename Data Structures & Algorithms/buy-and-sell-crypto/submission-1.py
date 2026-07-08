class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy = prices[0]
        sell = prices[0]
        max_profit = sell-buy
        for i in range(0,len(prices)):
            if(prices[i]<buy):
                buy=prices[i]
                sell = prices[i]
            if(prices[i]>sell):
                sell = prices[i]
            temp_profit = sell-buy
            if(temp_profit>max_profit):
                max_profit = temp_profit
        return max_profit
        