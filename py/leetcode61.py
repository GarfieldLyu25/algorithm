# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if head == None or head.next == None or k==0:
            return head
        n = 0
        p = head
        while p != None:
            n += 1
            p = p.next
        k = k % n
        if k == 0:
            return head
        dummy = ListNode(-1,head)
        fast = slow = dummy
        for i in range(k):
            fast = fast.next
        while fast.next != None:
            fast = fast.next
            slow = slow.next
        fast.next = dummy.next
        dummy.next = slow.next
        slow.next = None
        return dummy.next