class Solution:
    def levelOrder(self, root):
    # compact version using lc and without pop
        if not root:
            return []
        queue, result = [root], []
        while queue:
            level = [node.val for node in queue]
            result.append(level)
            queue = [child for node in queue for child in node.children if child]
        return result


"""https://leetcode.com/problems/n-ary-tree-level-order-traversal/discuss/148877/Python-5-lines-BFS-solution"""

# solution using any to handle edge case of root = [] is o(1) operation instead
# of o(n). Therefore, first 3 lines will be:

queue, result = [root], []
while any(queue):
