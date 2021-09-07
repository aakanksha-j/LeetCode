class TreeNode:
    def __init__(self, val, cnt = 1, left = None, right = None):
        self.val = val
        self.cnt = cnt
        self.left = left
        self.right = right

class KthLargest:
    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.root = None
        for num in nums:
            self.root = self.insert(self.root, num)

    def add(self, val: int) -> int:
        self.root = self.insert(self.root, val)
        return self.search()

    def insert(self, node, num):
        if not node:
            return TreeNode(num)

        node.cnt += 1
        if num < node.val:
            node.left = self.insert(node.left, num)
        else:
            node.right = self.insert(node.right, num)

        return node


    def search(self):
        count = self.k
        walker = self.root
        while count > 0:
            pos = 1 + (walker.right.cnt if walker.right else 0)
            if count == pos:
                break
            if count > pos:
                count -= pos
                walker = walker.left
            elif count < pos:
                walker = walker.right
        return walker.val


# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)

"""10 / 10 test cases passed, but took too long.
Time Complexities
h = height of tree with the average and best time O(log n) and worst time O(n)

Constructor O(nh)
Add O(h)
findKthLargest O(h)
https://leetcode.com/problems/kth-largest-element-in-a-stream/discuss/147729/O(h)-Java-Solution-Using-BST
https://leetcode.com/problems/kth-largest-element-in-a-stream/discuss/1160554/TLE-using-Leetcode's-solution
"""
