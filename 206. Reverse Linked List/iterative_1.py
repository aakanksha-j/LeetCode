# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        #iterative solution using prev and curr as temporary variables
        prev = None
        while head:
            curr = head # store current head in a temporary variable
            head = head.next # move the pointer to the next element
            curr.next = prev # reverse the temporary current head's next (for 2, next is 1 instead of 3)
            prev = curr # store the temporary variable in prev as for next iteration 2 will be prev for 3

        return prev
