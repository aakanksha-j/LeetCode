# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def return_alternate(self, node):
        return

    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return
        odd = head
        even = head.next
        while head.next:
            curr = head # assign dummy to head for odd
            cn = curr.next # assign dummy to head.next for even
            head = head.next # move head pointer
            curr.next = curr.next.next # counter for next
            #print(curr)
            #print(odd)
        #print(even)
        dummy = odd # to link odd and even, find end of odd
        while dummy.next is not None:
            dummy = dummy.next
        dummy.next = even
        return odd
