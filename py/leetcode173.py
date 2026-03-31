# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class BSTIterator:

    def __init__(self, root: Optional[TreeNode]):
        self.queue = collections.deque()
        self.inorder(root)

    def next(self) -> int:
        return self.queue.popleft()

    def hasNext(self) -> bool:
        return len(self.queue) > 0

    def inorder(self, root: Optional[TreeNode]):
        if not root:
            return
        self.inorder(root.left)
        self.queue.append(root.val)
        self.inorder(root.right)

# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()