class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        s0 = strs[0]
        for i,c in enumerate(s0):
            for str in strs:
                if i == len(str) or c != str[i]:
                    return s0[:i]
        return s0