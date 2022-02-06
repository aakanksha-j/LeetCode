# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        # using floyd cycle detection algorithm

        # make a ring of linkedlist A
        temp = headA
        while temp.next:
            temp = temp.next
        temp.next = headA

        # floyd's hare and tortoise pointers on linkedlist B
        fast, slow = headB, headB
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
            if fast == slow:
                slow2 = headB
                while slow != slow2:
                    slow = slow.next
                    slow2 = slow2.next
                temp.next = None
                return slow

        temp.next = None
        return None
