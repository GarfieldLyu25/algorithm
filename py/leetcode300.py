class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        n = len(nums)
        f = [1] * n
        for i in range(1,n):
            for j in range(i):
                if nums[i] > nums[j]:
                    f[i] = max(f[j] + 1,f[i])
        return max(f) #