"""
 作者 lgf
 日期 2025/8/6
"""
from typing import List
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        ans = 0
        inf = int(1e9)
        minprice = inf
        for i in prices:
            ans = max(i-minprice,ans)
            minprice = min(i,minprice)
        return ans