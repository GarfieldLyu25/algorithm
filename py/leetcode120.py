class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        n = len(triangle)
        f = triangle[-1][:]
        for i in range(n - 2, -1, -1):
            for j, x in enumerate(triangle[i]):
                f[j] = min(f[j], f[j + 1]) + x
        return f[0]