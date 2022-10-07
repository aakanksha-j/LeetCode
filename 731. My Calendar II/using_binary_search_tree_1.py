# https://leetcode.com/problems/my-calendar-ii/discuss/158747/Python-O(logN)
# https://leetcode.com/problems/my-calendar-ii/discuss/114882/Java-Binary-Search-Tree-method-clear-and-easy-to-undertand-beats-99
# https://leetcode.com/problems/my-calendar-iii/discuss/118470/My-python-solution-using-binary-search-tree

# time best O(log N) worst O(N)
# space O(N)


class Node(object):
    def __init__(self, start, end):
        self.s = start
        self.e = end
        self.k = 0
        self.left = self.right = None    
    
class MyCalendarTwo:

    def __init__(self):
        self.root = None
        
    def is_insertable(self, root, start, end):
        if start >= end:
            return True
        
        if not root:
            return True 
        else:
            if root.e <= start:
                return self.is_insertable(root.right, start, end)
            elif end <= root.s:
                return self.is_insertable(root.left, start, end)
            else:
                if root.k == 1:
                    return False
                elif root.s < start and end <= root.e:
                    return True
                else:
                    return self.is_insertable(root.left, start, root.s) and self.is_insertable(root.right, root.e, end)
    
    def insert(self, root, start, end):
        if start >= end:
            return root
        
        if not root:
            return Node(start, end)
        
        else:
            if root.e <= start:
                root.right = self.insert(root.right, start, end)
            elif end <= root.s:
                root.left = self.insert(root.left, start, end)
            else:
                a = min(root.s, start)
                b = max(root.s, start)
                c = min(root.e, end)
                d = max(root.e, end)
                
                root.left = self.insert(root.left, a, b)
                root.right = self.insert(root.right, c, d)
                                
                root.s = b
                root.e = c
                root.k = 1
            return root 
            

    def book(self, start: int, end: int) -> bool:
        if not self.is_insertable(self.root, start, end):
            return False
        self.root = self.insert(self.root, start, end)
        return True
        


# Your MyCalendarTwo object will be instantiated and called as such:
# obj = MyCalendarTwo()
# param_1 = obj.book(start,end)