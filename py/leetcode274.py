"""
 作者 lgf
 日期 2025/12/21
"""
class Solution:
    def hIndex(self, citations: List[int]) -> int:
        n = len(citations)
        cnt = [0] * (n + 1)
        for c in citations:
            cnt[min(c,n)] += 1
        ans = 0
        for i in range(n,-1,-1):
            ans += cnt[i]
            if ans >= i:
                return i