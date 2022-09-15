# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseLinkedlist(self, node):
        prev = None
        while node:
            curr = node
            node = node.next
            curr.next = prev
            prev = curr
        return prev

    def checkPalindrome(self, head, second_head):
        first, second = head, second_head
        while second:
            if first.val != second.val:
                return False
            first = first.next
            second = second.next
        return True

    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        # minimum no of nodes is 1 therefore no if head = None, return statement

        # step 1: determine the mid point of linked list
        fast = slow = head
        print(head)

        while fast and fast.next:
            # fast reaches null for even and last element for odd
            # slow reaches (3 in 12321) middle element for odd and (3 in 1231)
            # will run until fast.next becomes None (for [1,2,3,4,5,6] will run 3 times)
            # will run until fast.next becomes None (for [1,2,3,4,5,6,7] will run 4 times)
            fast = fast.next.next
            slow = slow.next
            #print('slow:', slow.val)
            #print('fast:', fast.val)

        # step 2: reverse the second half of the linked list
        #print('slow:', slow)
        second_head = self.reverseLinkedlist(slow)
        print(second_head) # two linked lists (1-2-3-4 and 7-6-5-4)

        # step 3: check whether it is a palindrome
        flag = self.checkPalindrome(head, second_head)
        print(second_head)

        # step 4: reverse the second half again to get the original linkedlist
        second_head = self.reverseLinkedlist(second_head)
        #slow.next = second_head - wrong code not needed.
        print(second_head)

        return flag
