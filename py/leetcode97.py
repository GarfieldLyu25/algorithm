class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        n, m = len(s1), len(s2)
        if n + m != len(s3):
            return False

        f = [[False] * (m + 1) for _ in range(n + 1)]
        f[0][0] = True
        for j, y in enumerate(s2):
            f[0][j + 1] = y == s3[j] and f[0][j]
        for i, x in enumerate(s1):
            f[i + 1][0] = x == s3[i] and f[i][0]
            for j, y in enumerate(s2):
                f[i + 1][j + 1] = x == s3[i + j + 1] and f[i][j + 1] or \
                                  y == s3[i + j + 1] and f[i + 1][j]

        return f[n][m]