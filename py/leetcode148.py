"""
 作者 lgf
 日期 2025/8/10
"""
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self,head: Optional[ListNode]) -> Optional[ListNode]:
        # 链表转数组
        arr = []
        cur = head
        while cur:
            arr.append(cur.val)
            cur = cur.next

        # 数组排序
        arr.sort()

        # 数组转链表
        dummy = ListNode()
        cur = dummy
        for val in arr:
            cur.next = ListNode(val)
            cur = cur.next
        return dummy.next