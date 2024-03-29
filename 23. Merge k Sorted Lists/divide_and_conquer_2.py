# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    """https://leetcode.com/problems/merge-k-sorted-lists/discuss/10919/Python-easy-to-understand-divide-and-conquer-solution."""
    def merge2lists(self, l, r):
        # recursive approach

        #print(l,r)
        if not l or not r:
            return l or r
        if l.val <= r.val:
            l.next = self.merge2lists(l.next, r)
            return l
        r.next = self.merge2lists(l, r.next)
        return r


    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        # divide and conquer approach
        # extra space of logk needed as it is bottom up approach to store l and r

        if not lists:
            return None

        if len(lists) == 1:
            return lists[0]

        mid = len(lists) // 2
        l, r = self.mergeKLists(lists[:mid]), self.mergeKLists(lists[mid:])
        return self.merge2lists(l, r)

#[[1,4,5],[1,3,4],[2,6],[2,7,8],[4,5],[7,9,10],[8,8,8]]

# The problem provides sample_input as a list, but when you run the problem via the website, the input is provided as actual ListNode.

# Below is an implementation of that you can use like lists = [ListNode.fromList(x) for x in sample_input]
