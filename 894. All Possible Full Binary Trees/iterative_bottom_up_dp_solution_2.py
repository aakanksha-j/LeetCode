"""
894. All Possible Full Binary Trees
Medium

Given an integer n, return a list of all possible full binary trees with n nodes. Each node of each tree in the answer must have Node.val == 0.

Each element of the answer is the root node of one possible tree. You may return the final list of trees in any order.

A full binary tree is a binary tree where each node has exactly 0 or 2 children.

Example 1:
Input: n = 7
Output: [[0,0,0,null,null,0,0,null,null,0,0],[0,0,0,null,null,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,null,null,null,null,0,0],[0,0,0,0,0,null,null,0,0]]

Example 2:
Input: n = 3
Output: [[0,0,0]]"""

# Definition for a binary tree node.
from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution:
    def allPossibleFBT(self, n: int) -> List[Optional[TreeNode]]:
        # iterative (bottom up) solution using dp array
        # time O(2^n)
        # space O(n.2^n/2)
        
        # base cases
        if n%2 == 0:
            return []
        
        dp = [[] for _ in range(n + 1)]
        dp[1].append(TreeNode())  # not [TreeNode(0)] because constructor already passes val=0
        
        
        for no_of_total_nodes in range(3, n + 1, 2): 
            for no_of_left_nodes in range(1, no_of_total_nodes - 1, 2):
                no_of_right_nodes = no_of_total_nodes - no_of_left_nodes - 1
                
                for left_node in dp[no_of_left_nodes]:
                    for right_node in dp[no_of_right_nodes]:
                        dp[no_of_total_nodes].append(TreeNode(0, left_node, right_node))
         
        return dp[n]