"""The problem is one step ahead of 380. Insert Delete GetRandom O(1).
There we used List and Dictionary of List {value: list(positions)}.
We swapped the deleting element with the last element in array.
We assigned index of deleting element to last element in hashmap.

However, here we cannot use a list to store positions in dictionary.
This is because to remove from a list takes O(n) time vs a set needs O(1) time. This is to take care of the edge case when the element we are deleting is the last element.
We cannot simply swap the values. Eg. [1,1,2,2,2] delete 1, 1, 2 will result in list index out of range error.
Therefore, these three lines are needed:

index_of_deleting_element = self.hashmap_set[val].pop() # pop
self.hashmap_set[last_element].add(index_of_deleting_element # add
self.hashmap_set[last_element].remove(index_of_last_element) # remove
I have taken inspiration from https://leetcode.com/problems/insert-delete-getrandom-o1-duplicates-allowed/discuss/1586322/Python-99.61-with-comments-use-dict-hash-and-a-list. They used defaultdict(set) to avoid key error issues. I have used basic dictionary. As a result, I need to delete empty set entries from hashmap and I don't need to check len(self.d[val]) > 0: for False conditions.

Runtime complexity: O(1) for all 3 methods
Space complexity: O(n), extra space needed for hashmap and array"""

class RandomizedCollection:
    # https://leetcode.com/problems/insert-delete-getrandom-o1-duplicates-allowed/discuss/1586322/Python-99.61-with-comments-use-dict-hash-and-a-list
    # remove method in set is O(1) and for list is O(n). Therefore, using a set to store positions in dictionary.
    # used two data structures - 1. List and 2. Dictionary containing values as key and their positions as values
    def __init__(self):
        self.hashmap_set = {}
        self.array = []

    def insert(self, val: int) -> bool:
        output = True
        
        if val in self.hashmap_set:
            self.hashmap_set[val].add(len(self.array))
            output = False
        else:
            self.hashmap_set[val] = {len(self.array)}
        
        self.array.append(val)
        return output
        
    def remove(self, val: int) -> bool:
        if val not in self.hashmap_set:
            return False
        
        # get index and value of last element
        print(self.array, self.hashmap_set)
        last_element = self.array[-1]
        index_of_last_element = len(self.array) - 1
        
        # remove deleting element from dictionary
        index_of_deleting_element = self.hashmap_set[val].pop()
        print(last_element, index_of_deleting_element)
        
        # add index of deleting element to last value's set first in dictionary
        # because of the edge case last value = deleting element
        self.hashmap_set[last_element].add(index_of_deleting_element)
        # then remove the last index from last element's set
        self.hashmap_set[last_element].remove(index_of_last_element)
       
        # swap in list
        self.array[index_of_deleting_element], self.array[index_of_last_element] = self.array[index_of_last_element], self.array[index_of_deleting_element]
        
        # remove deleting element from list and hashmap
        if len(self.hashmap_set[val]) == 0:
            del self.hashmap_set[val]
        self.array.pop()
        
        return True

    def getRandom(self) -> int:
        index = random.randint(0, len(self.array) - 1)
        return self.array[index]

	

# Your RandomizedCollection object will be instantiated and called as such:
# obj = RandomizedCollection()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()