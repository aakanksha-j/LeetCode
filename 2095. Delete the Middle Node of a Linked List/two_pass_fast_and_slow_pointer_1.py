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

# using for instead of while:
def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = fast = slow = ListNode(0, head)
        
        count = 0
        while fast and fast.next:
            fast = fast.next.next
            count += 1
            
        count = count * 2 if fast else (count*2 - 1)
        middle_index = count // 2
        
        for _ in range(middle_index): # as it is, not -1
            slow = slow.next
            
        slow.next = slow.next.next
        return dummy.next

# using single pass: fastest
def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next: return None
        
        slow = head
        fast = head.next.next # one step ahead
        
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            
        slow.next = slow.next.next
        return head


# using prev:
def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
    if not head.next: return None
        
    prev = None
    fast = slow = head
    
    while fast and fast.next:
        prev = slow
        slow = slow.next
        fast = fast.next.next
    
    prev.next = slow.next
    return head
    