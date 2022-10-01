# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        fast = slow = dummy = ListNode(-1)
        dummy.next = head
        count_len = 0
        while fast and fast.next:
            fast = fast.next.next
            count_len += 1
            
        len_lis = count_len*2 if fast else (count_len*2 - 1)
        k = len_lis // 2
        
        curr_count = -1
        while curr_count < k - 1:
            slow = slow.next
            curr_count += 1
            
        slow.next = slow.next.next
        return dummy.next
            
# time O(2n)
# space O(1)

# todo: figure out using single pass