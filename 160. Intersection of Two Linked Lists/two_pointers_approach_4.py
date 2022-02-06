"""visualization of the Solution https://leetcode.com/problems/intersection-of-two-linked-lists/discuss/49785/Java-solution-without-knowing-the-difference-in-len!"""
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        # two pointers solution
        # O(2(M+N)) time complexity and O(1) space complexity

        ptA, ptB = headA, headB

        while ptA != ptB:
            #print('ptA before', ptA.val)
            ptA = headB if ptA is None else ptA.next
            #print('ptA after', ptA.val)
            ptB = headA if ptB is None else ptB.next

        return ptB
