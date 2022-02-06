# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        # leetcode solution using set instead of dictionary for extra space
        # here instead of dictionary we use set

        nodes_in_B = set()

        while headB:
            nodes_in_B.add(headB) # add method for set instead of append
            headB = headB.next

        while headA:
            if headA in nodes_in_B:
                return headA
            headA = headA.next

        return None

"""Leetcode solution using brute force.
# brute force approach: compare each value of A with each value of B, 2 while loops
        while headA:
            ptB = headB
            while ptB:
                if headA == ptB:
                    return headA
                ptB = ptB.next
            headA = headA.next

        return None
"""
