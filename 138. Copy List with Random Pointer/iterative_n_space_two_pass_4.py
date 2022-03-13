"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        # neetcode solution

        deepcopy = {None: None} # if none not mentioned, then Keyerror: None

        # 1st pass: create nodes
        cur = head
        while cur:
            node = Node(cur.val)
            deepcopy[cur] = node
            cur = cur.next

        # 2nd pass: link next and random pointers
        cur = head
        while cur:
            node = deepcopy[cur] # similar to cur = head
            node.next = deepcopy[cur.next]
            node.random = deepcopy[cur.random]
            cur = cur.next

        return deepcopy[head]

"""There are 3 solutions provided by Leetcode. 1. Recursive with O(n) space
using dictionary, 2. Iterative with O(n) space using dictionary and 3. Iterative
using O(1) space. In neetcode solution, we use dictionary and O(n) space and
2 pass running while loop twice, once to create nodes and again to assign
pointers. This solution is more intuitive compared to leetcode's 2nd Iterative
solution where we call separate function.
Time complexity is O(n)"""
