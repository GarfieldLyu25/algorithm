"""
 作者 lgf
 日期 2025/12/21
"""
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        for i in range(1,len(prices)):
            profit+=max(0,prices[i]-prices[i-1])
        return profit


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        f0,f1 = 0, -inf
        for p in prices:
            f0 = max(f0,f1 + p)
            f1 = max(f1,f0 - p)
        return f0