# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        # approach 1
        if not head:
            return
        first, second = head, head.next if head else None
        while second:
            if second.val == val:
                first.next = second.next
                second = first.next
            else:
                first = second
                second = second.next
        return head if head.val != val else head.next

        # approach 2
        if not head:
            return
        curr = head if head else None
        while curr.next:
            if curr.next.val == val:
                curr.next = curr.next.next
            else:
                curr = curr.next
        return head if head.val != val else head.next
