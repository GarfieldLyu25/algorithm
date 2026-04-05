class Solution:
    def totalNQueens(self, n: int) -> int:
        ans = 0
        col = [False] * n
        diag1 = [False] * (n * 2 - 1)
        diag2 = [False] * (n * 2 - 1)

        def dfs(r: int) -> None:
            if r == n:
                nonlocal ans
                ans += 1
                return
            for c, ok in enumerate(col):
                if not ok and not diag1[r + c] and not diag2[r - c]:
                    col[c] = diag1[r + c] = diag2[r - c] = True
                    dfs(r + 1)
                    col[c] = diag1[r + c] = diag2[r - c] = False  # 恢复现场

        dfs(0)
        return ans 