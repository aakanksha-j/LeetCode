# https://leetcode.com/problems/my-calendar-iii/discuss/118470/My-python-solution-using-binary-search-tree

# time O(N^2)
# space O(N)

class Node(object):
    def __init__(self, start, end, ktime = 1):
        self.s = start
        self.e = end
        self.k = ktime
        self.left = None
        self.right = None
    
    
class MyCalendarThree:
    def __init__(self):
        self.root = None
        self.k = 0
        
    def insert(self, root, start, end, k):
        if start >= end:
            return root
        if not root:
            self.k = max(self.k, k)
            return Node(start, end, k)
        else:
            if root.e <= start:
                root.right = self.insert(root.right, start, end, k)
                return root
            elif end <= root.s:
                root.left = self.insert(root.left, start, end, k)
                return root
            else:
                a = min(root.s, start)
                b = max(root.s, start)
                c = min(root.e, end) 
                d = max(root.e, end) 
                
                root.left = self.insert(root.left, a, b, a == root.s and root.k or k)
                root.right = self.insert(root.right, c, d, d == root.e and root.k or k)
                
                root.s = b
                root.e = c
                root.k += k
                
                self.k = max(self.k, root.k)
                return root

    def book(self, start: int, end: int) -> int:
        """
        :type start: int
        :type end: int
        :rtype : int
        """
        self.root = self.insert(self.root, start, end, 1)
        return self.k


# Your MyCalendarThree object will be instantiated and called as such:
# obj = MyCalendarThree()
# param_1 = obj.book(start,end)