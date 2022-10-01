# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapNodes(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        fast = slow =dummy = ListNode(0, head)
        
        for i in range(k):
            fast = fast.next
            
        front = fast
        
        while fast.next:
            fast, slow = fast.next, slow.next
            
        end = slow.next
        
        front.val, end.val = end.val, front.val
        
        return dummy.next
        
# time O(N) - size of linked list
# space O(1)