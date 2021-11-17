https://leetcode.com/problems/design-linked-list/discuss/702777/Java-Solution-using-Doubly-LinkedList-7-ms-faster-than-96.65

class Node:
    def  __init__(self, val):
        self.val = val
        self.next = None
        self.prev = None

class MyLinkedList:

    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def get(self, index: int) -> int:
        if index < 0 or index >= self.size:
            return -1

        if not self.head:
            return -1

        if index == 0:
            return self.head.val
        elif index == self.size - 1:
            return self.tail.val
        else:
            curr = self.head
            for ind in range(index):
                curr = curr.next
            return curr.val

    def addAtHead(self, val: int) -> None:
        self.addAtIndex(0, val)

    def addAtTail(self, val: int) -> None:
        self.addAtIndex(self.size, val)

    def addAtIndex(self, index: int, val: int) -> None:
        if index < 0 or index > self.size:
            return

        node = Node(val)
        #print(index, val)
        if index== 0 or not self.head: # add value as the head of linked list
            node.next = self.head # important, missed earlier
            self.head = node
            if self.size == 0:
                self.tail = node

        elif index == self.size:
            node.prev = self.tail
            self.tail.next = node
            self.tail = node

        else:
            curr = self.head
            for _ in range(index - 1):
                curr = curr.next
            node.next = curr.next
            node.prev = curr
            curr.next.prev = node
            curr.next = node
            print(curr.next.prev.val)

        self.size += 1


    def deleteAtIndex(self, index: int) -> None:
        if index < 0 or index >= self.size:
            return

        print(index, self.head.val, self.head.next.val,self.size, self.tail.prev.val)
        if index == 0:
            self.head = self.head.next
            if self.head:
                self.head.prev = None
        elif index == self.size - 1:
            self.tail = self.tail.prev
            if self.tail:
                self.tail.next = None
        else:
            curr = self.head
            print(curr.val, curr.next.val, curr.prev.next.val)
            for _ in range(index):
                curr = curr.next
            curr.next.prev = curr.prev
            curr.prev.next = curr.next

        self.size -= 1
        print(curr.val)


# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)
