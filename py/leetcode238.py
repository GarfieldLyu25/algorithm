"""
 作者 lgf
 日期 2025/12/21
"""
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        fux = [1] * n
        for i in range(n-2,-1,-1):
            fux[i] = fux[i+1] * nums[i+1]
        pre = 1
        for i,c in enumerate(nums):
            fux[i] *= pre
            pre *= c
        return fux
