# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        nL1 = ListNode(-1)
        t1 = nL1
        nL2 = ListNode(-1)
        t2 = nL2
        while head:
            if head.val < x:
                t1.next = ListNode(head.val)
                t1 = t1.next
            else:
                t2.next = ListNode(head.val)
                t2 = t2.next
            head = head.next
        t1.next = nL2.next
        return nL1.next