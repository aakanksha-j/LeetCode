# Definition for singly-linked list.
#class ListNode:
#   def __init__(self, val=0, next=None):
#        self.val = val
#        self.next = next
class Solution:
    def mergeTwoLists(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        head = ListNode(0)
        point = head
        while l1 and l2:
            print(point)
            if l1.val <= l2.val:
                point.next = l1
                l1 = l1.next
            else:
                point.next = l2
                l2 = l2.next
            point = point.next
        if l1:
            point.next = l1
        else:
            point.next = l2
        return head.next

# space complexity: O(1)
# time complexity: O(n) number of elements in linked list
