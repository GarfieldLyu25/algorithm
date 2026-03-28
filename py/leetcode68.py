class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        ans = []
        n = len(words)
        i = 0
        while i < n:
            start = i
            sum_len = -1
            while i < n and sum_len + len(words[i]) + 1 <= maxWidth:
                sum_len += len(words[i]) + 1
                i += 1

            extra_spaces = maxWidth - sum_len
            gaps = i - start - 1

            if gaps == 0 or i == n:
                row = ' '.join(words[start:i]) + ' ' * extra_spaces
                ans.append(row)
                continue

            avg, rem = divmod(extra_spaces, gaps)
            spaces = ' ' * (avg + 1)
            row = (spaces + ' ').join(words[start:start + rem + 1]) + \
                  spaces + spaces.join(words[start + rem + 1:i])
            ans.append(row)
        return ans