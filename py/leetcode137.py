class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        ans = 0
        for i in range(31):
            cnt1 = sum(x >> i & 1 for x in nums)
            ans |= cnt1 % 3 << i
        cnt1 = sum(x >> 31 & 1 for x in nums)
        return ans - (cnt1 % 3 << 31)


class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        a = b = 0
        for x in nums:
            b = (b ^ x) & ~a
            a = (a ^ x) & ~b
        return b

