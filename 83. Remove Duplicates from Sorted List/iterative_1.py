#https://leetcode.com/problems/remove-duplicates-from-sorted-list/discuss/28699/Clear-Python-Code-(-beat-90-)
class Solution:
    def deleteDuplicates(self, head):
        #using 2 variables for head and head.next
        first, second = head, head.next if head else None
        while first and second:
            if first.val == second.val:
                first.next = second.next
                second = first.next
            else:
                first = second
                second = second.next
        return head

        #using single variable for head
        curr = head if head else None
        while curr.next:
            if curr.val == curr.next.val:
                curr.next = curr.next.next
            else:
                curr = curr.next
        return head
