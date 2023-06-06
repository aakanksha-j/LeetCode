"""
1376. Time Needed to Inform All Employees
Medium
A company has n employees with a unique ID for each employee from 0 to n - 1. The head of the company is the one with headID.

Each employee has one direct manager given in the manager array where manager[i] is the direct manager of the i-th employee, manager[headID] = -1. Also, it is guaranteed that the subordination relationships have a tree structure.

The head of the company wants to inform all the company employees of an urgent piece of news. He will inform his direct subordinates, and they will inform their subordinates, and so on until all employees know about the urgent news.

The i-th employee needs informTime[i] minutes to inform all of his direct subordinates (i.e., After informTime[i] minutes, all his direct subordinates can start spreading the news).

Return the number of minutes needed to inform all the employees about the urgent news.

 

Example 1:

Input: n = 1, headID = 0, manager = [-1], informTime = [0]
Output: 0
Explanation: The head of the company is the only employee in the company.
Example 2:


Input: n = 6, headID = 2, manager = [2,2,-1,2,2,2], informTime = [0,0,1,0,0,0]
Output: 1
Explanation: The head of the company with id = 2 is the direct manager of all the employees in the company and needs 1 minute to inform them all.
The tree structure of the employees in the company is shown.
 

Constraints:

1 <= n <= 105
0 <= headID < n
manager.length == n
0 <= manager[i] < n
manager[headID] == -1
informTime.length == n
0 <= informTime[i] <= 1000
informTime[i] == 0 if employee i has no subordinates.
It is guaranteed that all the employees can be informed."""

# Approach:
# Create an adjacency list to map {manager : [subordinate1, subordinate2]} relationship.
# Create a queue with headID
# Use variable self.output to store maximum value reached so far.
# Run BFS by iterating over node and adding all the edges.

# References:

# Neetcode (https://www.youtube.com/watch?v=zdBYi0p4L5Q&ab_channel=NeetCodeIO)
# https://leetcode.com/problems/time-needed-to-inform-all-employees/discuss/532530/Python3-Easy-Python-Solution%3A-DijkstraBFSDFS


# Test cases:
# n = 11, headID = 4, manager = [5,9,6,10,-1,8,9,1,9,3,4], informTime = [0,213,0,253,686,170,975,0,261,309,337]
# n =15, headID = 0, manager = [-1,0,0,1,1,2,2,3,3,4,4,5,5,6,6], informTime = [1,1,1,1,1,1,1,0,0,0,0,0,0,0,0]

# Both approaches take O(n) time and space

# Iterative BFS
from ast import List
from collections import defaultdict


class Solution:
    def numOfMinutes(self, n: int, headID: int, manager: List[int], informTime: List[int]) -> int:
        adj = defaultdict(list)
        for i in range(n):
            adj[manager[i]].append(i)
        output = 0
        queue = deque([(headID, 0)])
        while queue:
            # for _ in range(len(queue)): not needed as it is tree, not graph, so unidirectional
                node, time = queue.popleft()
                output = max(output, time) 
                for edge in adj[node]:
                    queue.append((edge, time + informTime[node]))
        return output

# Recursive DFS
class Solution:
    def numOfMinutes(self, n: int, headID: int, manager: List[int], informTime: List[int]) -> int:
        adj = defaultdict(list)
        for i in range(n):
            adj[manager[i]].append(i)
        self.output = 0
        def dfs(manager, time):
                self.output = max(self.output, time) 
                for subordinate in adj[manager]:
                    dfs(subordinate, time + informTime[manager])
        dfs(headID, 0)
        return self.output