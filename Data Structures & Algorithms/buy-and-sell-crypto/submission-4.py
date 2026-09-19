class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        max_price, min_price = float("-inf"), float("inf")

        for price in prices:
            min_price = min(price, min_price)
            max_price = max(max_price, price - min_price)

        return max_price