class MinStack:
    """Runtime: 612 ms
       Memory: 17.9 MB"""

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.items = []

    def push(self, x: int) -> None:
        self.items.append(x)

    def pop(self) -> None:
        if len(self.items) != 0:
            self.items.pop()
        return None

    def top(self) -> int:
        return self.items[len(self.items)-1]

    def getMin(self) -> int:
        if len(self.items) != 0:
            return min(self.items)
        else:
            return None

# Your MinStack object will be instantiated and called as such:
obj = MinStack()
obj.push(-2)
obj.push(0)
obj.push(-3)
obj.pop()
param_3 = obj.top()
param_4 = obj.getMin()
