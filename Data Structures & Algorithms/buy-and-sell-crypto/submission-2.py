class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_price = float('inf')
        max_profit = 0
        
        for price in prices:
            if price < min_price:
                min_price = price  # Found a cheaper day to buy
            elif price - min_price > max_profit:
                max_profit = price - min_price  # Found a better profit window
                
        return max_profit
