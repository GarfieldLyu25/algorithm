class Solution:
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        h = [(nums1[0] + nums2[0], 0, 0)]
        ans = []
        for _ in range(k):
            _, i, j = heappop(h)
            ans.append([nums1[i],nums2[j]])
            if j == 0 and i + 1 < len(nums1):
                heappush(h, (nums1[i + 1]+nums2[0],i + 1,0))
            if j + 1 < len(nums2):
                heappush(h, (nums1[i] + nums2[j + 1], i, j + 1))
        return ans