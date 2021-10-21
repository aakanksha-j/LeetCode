# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return
        odd = head
        even = head.next
        evenHead = even
        while even and even.next:
            print(head)
            odd.next = odd.next.next
            even.next = even.next.next
            odd = odd.next
            even = even.next
            print('odd:', odd)
            print('even:', even)
        odd.next = evenHead
        return head

#https://leetcode.com/problems/odd-even-linked-list/discuss/133345/With-detailed-explanation-or-Python
