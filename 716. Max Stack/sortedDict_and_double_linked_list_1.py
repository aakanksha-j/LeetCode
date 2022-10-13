from sortedcontainers import SortedDict

class Node:
    def __init__(self, val = None):
        self.val= val
        self.next = None
        self.prev = None        
    
class DoubleLinkedList:
    def __init__(self):
        self.dummy_left = Node()
        self.dummy_right = Node()
        self.dummy_left.next = self.dummy_right
        self.dummy_right.prev = self.dummy_left
        
    def append(self, node) -> None:
        left = self.dummy_right.prev 
        right = self.dummy_right
        
        node.prev = left
        node.next = right
        
        left.next = node
        right.prev = node
        
    def peek(self) -> int:
        return self.dummy_right.prev.val
    
    def remove(self, node) -> int:
        left = node.prev
        right = node.next
        
        left.next = right
        right.prev = left
        
        return node.val
    
    def pop(self) -> int:
        return self.remove(self.dummy_right.prev)
    
class MaxStack:
    # O(1)
    def __init__(self):
        self.max_stack = DoubleLinkedList()
        self.treemap = SortedDict({}) # {int x: [node_stack]}           
    
    # O(logn)
    def push(self, x: int) -> None:
        node = Node(x)
        self.max_stack.append(node)
        node_stack = self.treemap.setdefault(x, []) # O(logn)
        node_stack.append(node)
        
    # O(1)
    def top(self) -> int:
        return self.max_stack.peek()
    
    # O(logn)
    def peekMax(self) -> int:
        return self.treemap.peekitem()[0]        

    # O(logn)
    def pop(self) -> int:
        val = self.max_stack.pop()
        self.__pop_treemap(val)        
        return val
    
    # O(logn)
    def popMax(self) -> int:
        max_val = self.peekMax()
        node = self.__pop_treemap(max_val)
        return self.max_stack.remove(node)
    
    # O(logn)
    def __pop_treemap(self, val) -> int:
        node_stack = self.treemap[val]
        node = node_stack.pop()
        if not node_stack:
            del self.treemap[node.val]
        return node
            
        
# Your MaxStack object will be instantiated and called as such:
# obj = MaxStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.peekMax()
# param_5 = obj.popMax()

# https://leetcode.com/problems/max-stack/discuss/1633621/Python-easy-to-understand-solution-using-SortedDict-and-DoubleLinkedList
