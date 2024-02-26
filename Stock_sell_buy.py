class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        current_max_val = 0
        potential_profit = 0
        max_profit_val = 0

        for price in reversed(prices):
            # Update the current maximum value with the maximum of the current value and the previous maximum
            current_max_val = max(current_max_val, price)
            
            # Calculate the potential profit by subtracting the current price from the current maximum value
            potential_profit = current_max_val - price
            
            # Update the maximum profit with the maximum of the potential profit and the previous maximum profit
            max_profit_val = max(potential_profit, max_profit_val)
        return max_profit_val
