# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        # Floyd's cycle detection algorithm using fast and slow pointers

        # edge case missed where the list is empty
        if not head:
            return False

        fast, slow = head, head
        # always write fast and fast.next becoause if there is no cycle then
        # only fast.next will result in runtime 'Nonetype' error.
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
            if fast == slow:
                slow2 = head
                while slow != slow2:
                    slow = slow.next
                    slow2 = slow2.next
                return True

        return False



def main():
    numbers = [3,2,0,-4]
    pos = 1
    s=Solution()
    print(s.hasCycle(numbers))
    numbers = [1,2]
    pos = 0
    print(s.hasCycle(numbers))
    numbers = [1]
    pos = -1
    print(s.hasCycle(numbers))

if __name__ == '__main__':
    main()
