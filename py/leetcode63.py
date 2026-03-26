class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        m, n = len(obstacleGrid), len(obstacleGrid[0])
        f = [[0] * (n + 1) for _ in range(m + 1)]
        f[0][1] = 1
        for i, row in enumerate(obstacleGrid):
            for j, x in enumerate(row):
                if x == 0:
                    f[i + 1][j + 1] = f[i][j + 1] + f[i + 1][j]
        return f[m][n]