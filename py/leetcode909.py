class Solution:
    def snakesAndLadders(self, board: List[List[int]]) -> int:
        n = len(board)
        vis = [False] * (n * n + 1)
        vis[1] = True
        q = [1]
        step = 0
        while q:
            tmp = q
            q = []
            for x in tmp:
                if x == n * n:
                    return step
                for y in range(x + 1, min(x + 6, n * n) + 1):
                    r, c = divmod(y - 1, n)
                    if r % 2:
                        c = n - 1 - c
                    nxt = board[-1-r][c]
                    if nxt < 0:
                        nxt = y
                    if not vis[nxt]:
                        vis[nxt] = True
                        q.append(nxt)
            step += 1
        return -1