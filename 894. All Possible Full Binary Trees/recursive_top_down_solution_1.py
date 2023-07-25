# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def allPossibleFBT(self, n: int) -> List[Optional[TreeNode]]:
        # recursive (top down) solution using memoization
        # time O(2^n)
        # space O(n.2^n/2)
        
        # dp = {0: [], 1: [TreeNode()]}
        
        # base cases
        # if n in dp:
        #     return dp[n]
        if n%2 == 0:
            return []
        if n == 1: 
            return [TreeNode()]  # not [TreeNode(0)] because constructor already passes val=0
        
        res = []
        for i in range(1, n, 2):
            left_trees, right_trees = self.allPossibleFBT(i), self.allPossibleFBT(n-i-1)
            
            for t1 in left_trees:
                for t2 in right_trees:
                    res.append(TreeNode(0, t1, t2))
            
        # dp[n] = res
        return res