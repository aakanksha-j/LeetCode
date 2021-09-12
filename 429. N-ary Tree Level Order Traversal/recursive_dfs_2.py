class Solution:
    # using recursion and dfs
    def dfs(self, root, level, res):
        if root:
            if len(res) < level + 1:
                res.append([])
            for child in root.children:
                self.dfs(child, level + 1, res)
            res[level].append(root.val)

    def levelOrder(self, root):
        ans = []
        self.dfs(root, 0, ans)
        return ans
