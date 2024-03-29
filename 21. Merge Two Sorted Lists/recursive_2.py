# Definition for singly-linked list.
#class ListNode:
#   def __init__(self, val=0, next=None):
#        self.val = val
#        self.next = next
class Solution:
    def mergeTwoLists(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        #recursive approach
        if l2 is None:
            return l1
        if l1 is None:
            return l2
        if l1.val <= l2.val:
            l1.next = self.mergeTwoLists(l1.next, l2)
            return l1
        else:
            l2.next = self.mergeTwoLists(l1, l2.next)
            return l2
