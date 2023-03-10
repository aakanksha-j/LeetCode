"""Given a singly linked list, return a random node's value from the linked list. Each node must have the same probability of being chosen.

Implement the Solution class:

Solution(ListNode head) Initializes the object with the head of the singly-linked list head.
int getRandom() Chooses a node randomly from the list and returns its value. All the nodes of the list should be equally likely to be chosen.
 

Example 1:


Input
["Solution", "getRandom", "getRandom", "getRandom", "getRandom", "getRandom"]
[[[1, 2, 3]], [], [], [], [], []]
Output
[null, 1, 3, 2, 2, 3]

Explanation
Solution solution = new Solution([1, 2, 3]);
solution.getRandom(); // return 1
solution.getRandom(); // return 3
solution.getRandom(); // return 2
solution.getRandom(); // return 2
solution.getRandom(); // return 3
// getRandom() should return either 1, 2, or 3 randomly. Each element should have equal probability of returning.
 

Constraints:

The number of nodes in the linked list will be in the range [1, 104].
-104 <= Node.val <= 104
At most 104 calls will be made to getRandom.
 

Follow up:

What if the linked list is extremely large and its length is unknown to you?
Could you solve this efficiently without using extra space?"""

"""Approach: without array, just get the length of linked list, constant space

    # runtime complexity O(n) for init method, O(n) for getRandom method
    # space complexity O(1) as we don't need an array but we need length of linked list
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:

    def __init__(self, head: Optional[ListNode]):
        self.length = 0
        self.head = head
        node = head
        while node:
            self.length += 1
            node = node.next

    def getRandom(self) -> int:
        pick = random.randint(0, self.length - 1) # length - 1, otherwise out of index error
        print(pick)
        node = self.head
        while pick:
            node = node.next
            pick -= 1
            
        return node.val

# Your Solution object will be instantiated and called as such:
# obj = Solution(head)
# param_1 = obj.getRandom()