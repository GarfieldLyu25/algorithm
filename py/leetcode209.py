class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        n =len(nums)
        ans = inf
        s = left = 0
        for right,x in enumerate(nums):
            s += x
            while s >= target:
                ans = min(ans, right - left + 1)
                s -= nums[left]
                left += 1
        return ans if ans <= n else 0