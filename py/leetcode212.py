class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        def buildTrie(words) -> Dict:
            trie = {}
            for word in words:
                node = trie
                for ch in word:
                    node = node.setdefault(ch, {})
                node[WORD] = word
            return trie

        def dfs(r, c, trie: Dict) -> None:
            ch = board[r][c]
            if ch not in trie:
                return

            node = trie[ch]
            match = node.pop(WORD, None)
            if match:
                res.add(match)

            board[r][c] = '*'
            if r > 0:
                dfs(r - 1, c, node)
            if r < rows - 1:
                dfs(r + 1, c, node)
            if c > 0:
                dfs(r, c - 1, node)
            if c < cols - 1:
                dfs(r, c + 1, node)

            board[r][c] = ch
            if not trie[ch]:
                del trie[ch]

        WORD = '$'
        trie = buildTrie(words)
        rows, cols = len(board), len(board[0])
        res = set()
        for r in range(rows):
            for c in range(cols):
                if board[r][c] in trie:
                    dfs(r, c, trie)
        return list(res)