# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    # iterative inorder solution - https://leetcode.com/problems/convert-sorted-list-to-binary-search-tree/discuss/1244022/Python-O(N)-Iterative-with-stack-Need-NOT-to-convert-to-Array

    # time: O(N) - visit every node
    # space: O(N) - stack

    def find_len(self, head):
        curr = head
        n = 0
        while curr:
            n += 1
            curr = curr.next
        return n

    def sortedListToBST(self, head: Optional[ListNode]) -> Optional[TreeNode]:
        if not head: return None

        n = self.find_len(head)

        curr = head
        root = TreeNode(-1)
        stack = [(0, n-1, root, False)]

        while stack:
            start, end, node, status = stack.pop()

            mid = (start + end) // 2 # always choose left node as root

            if status is False:
                # inorder traversal
                if mid + 1 <= end:
                    node.right = TreeNode(-1)
                    stack.append((mid+1, end, node.right, False))
                stack.append((start, end, node, True))
                if start <= mid - 1:
                    node.left = TreeNode(-1)
                    stack.append((start, mid-1, node.left, False))

            else:
                node.val = curr.val
                curr = curr.next

        return root
