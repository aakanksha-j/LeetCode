# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteRootNode(self, root: TreeNode):
        if not root:
            return None

        # one of the child is None
        if not root.left:
            return root.right
        if not root.right:
            return root.left

        # both the children are present
        next = root.right
        pre = None
        while next.left:
            pre = next
            next = next.left
        next.left = root.left
        if next != root.right:
            pre.left = next.right
            next.right = root.right
        return next

    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        pre = None
        cur = root
        while cur and cur.val != key: # binary search
            pre = cur
            if key < cur.val:
                cur = cur.left
            #print(cur.val)
            elif key > cur.val:
                cur = cur.right
        if not pre: # loop did not run once, key == cur
            return self.deleteRootNode(cur)
        if pre.left == cur:
            pre.left = self.deleteRootNode(cur)
        else:
            pre.right = self.deleteRootNode(cur)
        return root # key not found, return the root as is.

"""[40,20,60,10,30,50,70,null,null,25,35] key =20
https://leetcode.com/problems/delete-node-in-a-bst/discuss/93298/Iterative-solution-in-Java-O(h)-time-and-O(1)-space

Find the node to be removed and its parent using binary search, and then use
deleteRootNode to delete the root node of the subtree and return the new root
node. This idea is taken from
https://discuss.leetcode.com/topic/67309/an-easy-understanding-o-h-time-o-1-space-java-solution."""
