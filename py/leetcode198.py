class Solution:
    def rob(self, nums: List[int]) -> int:
        if not nums:
            return 0
        n = len(nums)
        if n == 1:
            return nums[0]
        f = [0] * len(nums)
        f[0] = nums[0]
        f[1] = max(nums[0],nums[1])
        for i in range(2,n):
            f[i] = max(f[i-1],nums[i]+f[i-2])
        return f[n-1]