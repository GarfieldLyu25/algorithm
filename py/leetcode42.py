class Solution:
    def trap(self, height: List[int]) -> int:
        ans = 0
        leftMax = rightMax = left = 0
        right = len(height) - 1
        while left < right:
            leftMax = max(leftMax,height[left])
            rightMax = max(rightMax,height[right])
            if height[left] < height[right]:
                ans += leftMax - height[left]
                left += 1
            else:
                ans += rightMax - height[right]
                right -= 1
        return ans