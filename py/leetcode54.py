DIRS = (0, 1), (1, 0), (0, -1), (-1, 0)  # 右下左上
"""
n
m - 1
n - 1
m - 2
"""
class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        m, n = len(matrix), len(matrix[0])
        size = m * n
        ans = []
        i, j, di = 0, -1, 0
        while len(ans) < size:
            dx, dy = DIRS[di]
            for _ in range(n):
                i += dx
                j += dy
                ans.append(matrix[i][j])
            di = (di + 1) % 4
            n, m = m - 1, n  # 减少后面的循环次数（步数）
        return ans

