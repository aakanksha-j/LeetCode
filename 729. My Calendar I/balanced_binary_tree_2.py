"""Intuition
If we maintained our events in sorted order, we could check whether an event could be booked in O(logN) time
(where N is the number of events already booked) by binary searching for where the event should be placed.
We would also have to insert the event in our sorted structure.

Algorithm
We need a data structure that keeps elements sorted and supports fast insertion.

In Java, a TreeMap is the perfect candidate.

In Python, we can build our own binary tree structure.

For Java, we will have a TreeMap where the keys are the start of each interval,
and the values are the ends of those intervals.
When inserting the interval [start, end), we check if there is a conflict
on each side with neighboring intervals:
we would like calendar.get(prev)) <= start <= end <= next for the booking to be valid
(or for prev or next to be null respectively.)

For Python, we will create a binary tree. Each node represents some interval [self.start, self.end)
while self.left, self.right represents nodes that are smaller or larger than the current node.

Time Complexity (Java): O(NlogN), where N is the number of events booked.
For each new event, we search that the event is legal in O(logN) time, then insert it in O(1) time.

Time Complexity (Python): O(N^2) worst case, with O(NlogN) on random data.
For each new event, we insert the event into our binary tree.
As this tree may not be balanced, it may take a linear number of steps to add each event.

Space Complexity: O(N), the size of the data structures used."""

class Node:
    def __init__(self, start, end):
        self.start = start
        self.end = end
        self.left = self.right = None

    def insert(self, node):
        if node.start >= self.end:
            if not self.right:
                self.right = node
                return True
            return self.right.insert(node)
        elif node.end <= self.start:
            if not self.left:
                self.left = node
                return True
            return self.left.insert(node)
        else:
            return False

class MyCalendar(object):
    def __init__(self):
        self.root = None

    def book(self, start: int, end: int) -> bool:
        if self.root is None:
            self.root = Node(start, end)
            return True
        return self.root.insert(Node(start, end))

def main():
    obj = MyCalendar()
    param_1 = obj.book(10,20)
    print(param_1)
    param_2 = obj.book(20,30)
    print(param_2)
    param_3 = obj.book(15,25)
    print(param_3)


if __name__ == '__main__':
    main()
