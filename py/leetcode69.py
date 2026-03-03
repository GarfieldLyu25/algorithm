SQRT_MAX = isqrt(2 ** 31 -1)
class Solution:
    def mySqrt(self, x: int) -> int:
        left, right = 0, min(x, SQRT_MAX) + 1
        while left + 1 < right:
            m = (left + right) // 2
            if m * m <= x:
                left = m
            else:
                right = m
        return left