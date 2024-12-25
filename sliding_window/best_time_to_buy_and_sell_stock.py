# https://leetcode.com/problems/best-time-to-buy-and-sell-stock/
from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        """
        Given a list of prices where the i-th element is the price of a given stock on day i,
        this function calculates the maximum profit that can be achieved by buying and selling
        the stock. You must buy before you sell.

        Args:
            prices (List[int]): List of stock prices.

        Returns:
            int: The maximum profit that can be achieved.

        Example:
            >>> Solution().maxProfit([7,1,5,3,6,4])
            5
            >>> Solution().maxProfit([7,6,4,3,1])
            0
        """
        lowest = highest = prices[0]
        best_profit = 0
        for price in prices:
            if price < lowest:
                lowest = highest = price
            elif price > highest:
                highest = price
                best_profit = max(best_profit, highest - lowest)
        return best_profit
