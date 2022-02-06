# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def __init__(self):
        self.visited = {}

    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        # own approach using (hash) dictionary
        # O(N + M) time and O(N) space complexity
        ptA, ptB = headA, headB

        if not ptA.next and not ptB.next and ptA is ptB:
            return ptA

        while ptA: # had written ptA.next as was used to it for linked lists
            self.visited[ptA] = ptA.val
            ptA = ptA.next

        while ptB: # however if we wrote ptB.next, then last element will not be checked in dictionary
            if ptB in self.visited:
                return ptB
            ptB = ptB.next

        return None
