# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        # succinct iterative solution O(n) time, O(1) space

        dummy = jump = ListNode(0)
        dummy.next = l = r = head

        while True:
            count = 0
            while r and count < k: # use r to locate range
                r = r.next
                count += 1

            # if size k is satisfied, reverse inner linked list
            if count == k:

                # standard reversing a linked list - for k elements
                temp, prev = l, r
                for _ in range(k):
                    curr = temp
                    temp = temp.next
                    curr.next = prev
                    prev = curr

                # connext two k-groups
                jump.next = prev
                jump = l
                l = r
            else:
                return dummy.next

"""https://leetcode.com/problems/reverse-nodes-in-k-group/discuss/11491/Succinct-iterative-Python-O(n)-time-O(1)-space"""
