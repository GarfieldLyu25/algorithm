class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        st = []
        for token in tokens:
            if len(token) > 1 or token[0].isdigit():
                st.append(int(token))
                continue
            x = st.pop()
            if token == '+':
                st[-1] += x
            elif token == '-':
                st[-1] -= x
            elif token == '*':
                st[-1] *= x
            else:
                y = st[-1]
                q, r = divmod(y, x)
                if r and x * y < 0:
                    q += 1
                st[-1] = q
        return st[0]