# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        # own approach

        if not head or not head.next:
            return head

        n = 1 #length of linked list
        pointer = head
        while pointer.next: # run 1 loop till you reach the end of linked list
            pointer = pointer.next
            n += 1
        #print(n)

        #print(k)
        if k > n: # determine k in terms of less than length of linked list
            if k%n != 0:
                k = k%n
                print('1',k)
            else:
                k = 0
                return head
                print('2',k)
        #print(k)

        pointer.next = head # cteate a cycle in linked list

        count = 0  # find the new head and tail's location
        while count < n - k:
            pointer = pointer.next
            count += 1

        head = pointer.next # make new head
        pointer.next = None # cut off the cycle at new tail

        return head


"""# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        # mix of both own approach and leetcode solution
        # has better runtime and memory
        # base cases
        if not head or not head.next or k == 0:
            return head

        # close the linked list into a ring
        pointer = head
        n = 1
        while pointer.next:
            pointer = pointer.next
            n += 1

        if k % n == 0:
            return head

        pointer.next = head

        # find new tail: (n - (k % n))th node
        # find new head: (n - (k % n))th node
        # run for loop from tail
        for i in range(n - (k%n)):
            pointer = pointer.next
        head = pointer.next

        # break the ring
        pointer.next = None

        return head
"""
