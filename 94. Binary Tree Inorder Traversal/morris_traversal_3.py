def inorderTraversal(self, root: Treenode):
    res = []
    while root:
        # root has no left child
        if root.left == None:
            res.append(root.val)
            root = root.right
        # root has left child
        else:
            pre = root.left # create temp node for left node
            while pre.right != None:
                pre = pre.right # find the rightmost child of left node
            pre.right = root # make root the right node of rightmost child
            tmpNode = root # create temp node for root
            root = root.left # bring left node to the top
            tmpNode.left = None # avoid infinite loops by grounding tmpNode's left node.
        return res

# time complexity O(n) same as recursion and iteration
# space complexity O(1)
# input binary tree [1,2,3,4,5,6] output [4,2,5,1,6,3]
