class Solution:
    MAP = {
        'I':1,
        'V':5,
        'X':10,
        'L':50,
        'C':100,
        'D':500,
        'M':1000
    }

    def romanToInt(self, s: str) -> int:
        ans = 0
        for i,ch in enumerate(s):
            val = self.MAP[ch]
            if i < len(s)-1 and val < self.MAP[s[i+1]]:
                ans -= val
            else:
                ans += val
        return ans
