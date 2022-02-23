# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # two pass algorithm

        # using dummy node to handle two edge cases
        dummy = ListNode()
        dummy.next = head
        first, second, length = dummy, dummy, 0
        
        # first pass to determine length of linked list (L)
        while first.next:
            first = first.next
            length += 1

        print(length)

        # second pass to reach one node before nth node
        for _ in range(length - n): # eg. [1,2,3,4,5,6] n = 2, 6-2+1 = 5
        # range will go till 4 because python goes 1 less than specified
            second = second.next

        # remove nth node
        second.next = second.next.next
        return dummy.next
