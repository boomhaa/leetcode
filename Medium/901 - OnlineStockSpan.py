# link to the problem - https://leetcode.com/problems/online-stock-span/

# Design an algorithm that collects daily price quotes for some stock and returns the span of that stock's price for the current day.
# The span of the stock's price today is defined as the maximum number of consecutive days (starting from today and going backward) for which the stock price was less than or equal to today's price.
# For example, if the price of a stock over the next 7 days were [100,80,60,70,60,75,85], then the stock spans would be [1,1,1,2,1,4,6].
# Implement the StockSpanner class:
# StockSpanner() Initializes the object of the class.
# int next(int price) Returns the span of the stock's price given that today's price is price.

# link to submission - https://leetcode.com/submissions/detail/741618889/

class StockSpanner:

    def __init__(self):
        self.stack = []
        self.index = -1

    def next(self, price: int) -> int:
        self.index += 1
        while self.stack and self.stack[-1][0] <= price:
            self.stack.pop()
        ans = 0
        if self.stack:
            ans = self.index - self.stack[-1][1]
        else:
            ans = self.index + 1
        self.stack.append((price, self.index))
        return ans
