class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        ans = -inf
        sum = 0
        for x in nums:
            sum = max(sum, 0) + x
            ans = max(ans, sum)
        return ans
