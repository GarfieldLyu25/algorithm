# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        m = len(lists)
        if m == 0:
            return None
        step = 1
        while step < m:
            for i in range(0, m - step, step * 2):
                lists[i] = self.mergeTwoLists(lists[i],lists[i + step])
            step *= 2
        return lists[0]

    def mergeTwoLists(self,list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        cur = dummy = ListNode()
        while list1 and list2:
            if list1.val < list2.val:
                cur.next = list1
                list1 = list1.next
            else:
                cur.next = list2
                list2 = list2.next
            cur = cur.next
        cur.next = list1 or list2
        return dummy.next