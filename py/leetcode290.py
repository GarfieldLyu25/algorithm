class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        w2s, s2w  = {}, {}
        words = s.split()
        if len(pattern) != len(words):
            return False
        for ch,word in zip(pattern,words):
            if (word in w2s and w2s[word] != ch) or (ch in s2w and s2w[ch] != word):
                return False
            w2s[word] = ch
            s2w[ch] = word
        return True