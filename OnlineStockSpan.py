# 901. Online Stock Span
# https://leetcode.com/problems/online-stock-span/

class StockSpanner:
    def __init__(self):
        self.stack = list()
        self.curr = 0

    def next(self, price: int) -> int:
        self.curr += 1

        while self.stack and self.stack[-1][0] <= price:
            self.stack.pop()

        ans = self.curr - (self.stack[-1][1] if self.stack else 0)
        self.stack.append((price, self.curr))
        return ans

# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)