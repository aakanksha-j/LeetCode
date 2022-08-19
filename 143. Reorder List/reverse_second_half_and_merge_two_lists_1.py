# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    # time: O(N)
    # space: O(1)

    # made separate functions for reversing list and merging two lists

    def reverse_linked_list(self, slow):
        prev, curr = None, slow
        while curr:
            curr.next, prev, curr = prev, curr, curr.next
        return prev

    def merge_two_lists(self, head, second_head):
        l1, l2 = head, second_head
        while l2.next:
            l1.next, l1 = l2, l1.next
            l2.next, l2 = l1, l2.next

    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        # find midpoint using slow and fast pointers
        slow = fast = head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next

        # reverse second-half in-place
        second_head = self.reverse_linked_list(slow)

        # merge the two linked lists
        self.merge_two_lists(head, second_head)

        """
        # find midpoint using slow and fast pointers
        slow = fast = head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next

        # reverse second-half in-place
        prev, curr = None, slow # ans is in prev
        while curr:
            curr.next, prev, curr = prev, curr, curr.next

        # merge the two linked lists
        first, second = head, prev
        while second.next: #convert 1->2->3->4->5->6 into 1->2->3->4 and 6->5->4
            first.next, first = second, first.next
            second.next, second = first, second.next
        """    
