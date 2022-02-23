# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        # elementary math using dummy, carry and sum

        # declare pointers for both input lists and 1 output dummy list
        p1, p2 = l1, l2  # use separate pointers as we donot disturb original input
        head = dummy = ListNode() # no need to write ListNode(0) as definition has val = 0

        # add both lists
        carry = 0
        while p1 or p2:
            x = p1.val if p1 else 0
            y = p2.val if p2 else 0
            sum = x + y + carry
            carry = sum // 10 # 28/10 = 2.8 28//10 = 2
            dummy.next = ListNode(sum % 10)
            dummy = dummy.next
            if p1:
                p1 = p1.next
            if p2:
                p2 = p2.next

        # take care of carry
        if carry:
            dummy.next = ListNode(carry)

        return head.next
