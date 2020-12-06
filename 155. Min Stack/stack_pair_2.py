class MinStack:
    """Runtime: 56 ms
       Memory: 18.6 MB"""

    def __init__(self):
        """
        Use pair of (value, min_value) to store in stack.
        """
        self.stack = []

    def push(self, x: int) -> None:

        # if stack is empty, append and return right away.
        if not self.stack:
            self.stack.append((x,x))
            return

        # if stack is not empty, compare for min and then append
        current_min = self.stack[-1][1]
        self.stack.append((x, min(x, current_min)))

    def pop(self) -> None:
        self.stack.pop()

    def top(self) -> int:
        return self.stack[-1][0]

    def getMin(self) -> int:
        return self.stack[-1][1]

# Your MinStack object will be instantiated and called as such:
obj = MinStack()
obj.push(-2)
obj.push(0)
obj.push(-3)
obj.pop()
param_3 = obj.top()
print(param_3)
param_4 = obj.getMin()
print(param_4)
