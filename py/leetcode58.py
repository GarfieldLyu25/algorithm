class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        n = len(s) - 1
        while s[n] == ' ':
            n-=1
        ans = 0
        while s[n] != ' ' and n >= 0:
            n-=1
            ans+=1
        return ans