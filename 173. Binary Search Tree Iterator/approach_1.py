# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class BSTIterator:
    def __init__(self, root: TreeNode):
        self.stack = list()
        self.pushAll(root) # initialized to the smallest number in BS tree

    def pushAll(self, node): # adds elements to the stack, smallest element on top
        while node:
            self.stack.append(node)
            node = node.left

    def next(self) -> int: # pop the last element in stack, store as temp node and return
        tmpNode = self.stack.pop()
        self.pushAll(tmpNode.right) # add right elements to the stack
        return tmpNode.val

    def hasNext(self) -> bool:
        return self.stack # return whether a number exists to the right of pointer or not

# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()
