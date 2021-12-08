# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def merge2lists(self, list1, list2):
        head = point = ListNode(0)
        while list1 and list2:
            if list1.val < list2.val:
                point.next = list1
                list1 = list1.next
            else:
                point.next = list2
                list2 = list2.next
            point = point.next
        if list1:
            point.next = list1
        else:
            point.next = list2
        return head.next

    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        amount = len(lists)
        interval = 1
        while interval < amount:
            for i in range(0, amount - interval, interval*2):
                lists[i] = self.merge2lists(lists[i], lists[i + interval])
            interval *= 2
        return lists[0] if amount > 0 else None

"""
for loop conditions:
amount - interval: because if len of lists is 8 then pointer should go only till
6 and club 6,7 numbered list.
interval*2: because next list after 0 should be 2 as (0,1) are already clubbed.

later on when interval increases (eg. 4) then for loop range is (0,3,4). This will
combine list 0 and list 4 and for loop will stop there as end value is 3 and
interval is more than end value.


The complexity analysis here is a bit confusing, because N is the total number of nodes. If we express the complexity in the terms of average size of each list "n", it would be better to catch it (at least for me).
E.g. the Approach 4: Merge lists one by one. Say, for the sake of simplicity, all lists have the same size "n". At the first step of the algorithm we merge 2 lists with O(n) and get a list with size "2n". At the second step we merge a "2n" list with a "n" list, in the worse case we have to visit "2n" nodes and get a list with size "3n". And so on. At the end we have n + 2n + ... + kn = n(1+2 + .. + k) = n * k * (k + 1) / 2.
So in average we have here O(nk^2).
In the Approach 5 we have then O(nk*log(k)).
Don't confuse N and n on the real interview :)

Time complexity: n.k.log(k)
1. n = this part comes from merging 2 lists assuming each list is of average n size
2. k = this part comes from for loop to merge k lists
3. log k = this part comes from while loop with height k

Space complexity: O(1) because no extra space is needed to merge 2 lists."""
