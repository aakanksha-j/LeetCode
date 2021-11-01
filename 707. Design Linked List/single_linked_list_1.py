https://leetcode.com/problems/design-linked-list/discuss/139689/Python-solution

class Node:
    def  __init__(self, val):
        self.val = val
        self.next = None

class MyLinkedList:

    def __init__(self):
        self.head = None
        self.size = 0

    def get(self, index: int) -> int:
        if index < 0 or index >= self.size:
            return -1

        if not self.head:
            return -1

        curr = self.head
        for ind in range(index): # here we run upto index and not index + 1 as per range function which makes us go 1 more than size because index 0 is                 # considered in declaring curr as head
            # therefore for 1,2,3 index is 0,1,2 and 0 is already counted so only 2 more times run for loop
            # print(ind, curr.val)
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
        print(index, val)
        if index == 0 or not self.head: # add value as the head of linked list
            node.next = self.head # important, missed earlier
            self.head = node
        else:
            curr = self.head
            for _ in range(index - 1): # index - 1 because pointer is already at index = 0 therefore should be index, and we want to reach one place before                                        # index therefore index - 1
                curr = curr.next
            node.next = curr.next
            curr.next = node
        self.size += 1


    def deleteAtIndex(self, index: int) -> None:
        if index < 0 or index >= self.size:
            return
        curr = self.head
        #print(curr.val, curr.next.val, curr.next.next.val)
        if index == 0:
            self.head = curr.next
        else:
            for ind in range(index - 1): # index - 1 because head is already counted so index 0 is covered in above if statement
                #print(ind, curr.val)    # we want to reach one place before given index # eg for deleting 2 from 123 reach 1 from if stmt
                # and then do not run for loop as we want 1-->3 from curr.next = curr.next.next stmt
                curr = curr.next
            curr.next = curr.next.next
        self.size -= 1
        #print(curr.val)


# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)
