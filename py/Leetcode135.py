class Solution:
    def candy(self, ratings: List[int]) -> int:
        ans = n = len(ratings)
        i = 0
        while i < n:
            start = i - 1 if i > 0 and ratings[i - 1] < ratings[i] else i

            while i + 1 < n and ratings[i] < ratings[i + 1]:
                i += 1
            top = i

            while i + 1 < n and ratings[i] > ratings[i + 1]:
                i += 1

            inc = top - start
            dec = i - top
            ans += (inc*(inc-1) + dec*(dec-1)) // 2 + max(inc,dec)
            i += 1
        return ans


# 0 1 2 0 2 1 0
# 1 2 3 1 3 2 1