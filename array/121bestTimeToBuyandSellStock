# solution one

class Solution:
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        n = len(prices)
        if not prices or n == 0:
            return 0
        
        max_profit = 0
        min_price = prices[0]
        
        for i in range(1, n):
            max_profit = max(max_profit, prices[i] - min_price)
            min_price = min(min_price, prices[i])
            
        return max_profit
    
    #solution two
    
            profit = 0
        if prices:
            min = prices[0]
        for price in prices:
            if price < min:
                min = price
            else:
                sellProfit = price - min
                if sellProfit > profit:
                    profit = sellProfit
        return profit
