class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left, right = -1, len(nums) - 1
        while left + 1 < right:
            mid = (left + right) // 2
            x = nums[mid]
            if target > nums[-1] >= x:
                right = mid
            elif x > nums[-1] >= target:
                left = mid
            elif x >= target:
                right = mid
            else:
                left = mid
        return right if nums[right] == target else -1