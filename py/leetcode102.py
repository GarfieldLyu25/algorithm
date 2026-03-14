# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root is None:
            return []
        ans = []
        st = deque([root])
        while st:
            vals = []
            for _ in range(len(st)):
                node = st.popleft()
                vals.append(node.val)
                if node.left: st.append(node.left)
                if node.right: st.append(node.right)
            ans.append(vals)
        return ans