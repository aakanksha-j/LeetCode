"""Implement the RandomizedSet class:

RandomizedSet() Initializes the RandomizedSet object.
bool insert(int val) Inserts an item val into the set if not present. Returns true if the item was not present, false otherwise.
bool remove(int val) Removes an item val from the set if present. Returns true if the item was present, false otherwise.
int getRandom() Returns a random element from the current set of elements (it's guaranteed that at least one element exists when this method is called). Each element must have the same probability of being returned.
You must implement the functions of the class such that each function works in average O(1) time complexity.

 

Example 1:

Input
["RandomizedSet", "insert", "remove", "insert", "getRandom", "remove", "insert", "getRandom"]
[[], [1], [2], [2], [], [1], [2], []]
Output
[null, true, false, true, 2, true, false, 2]

Explanation
RandomizedSet randomizedSet = new RandomizedSet();
randomizedSet.insert(1); // Inserts 1 to the set. Returns true as 1 was inserted successfully.
randomizedSet.remove(2); // Returns false as 2 does not exist in the set.
randomizedSet.insert(2); // Inserts 2 to the set, returns true. Set now contains [1,2].
randomizedSet.getRandom(); // getRandom() should return either 1 or 2 randomly.
randomizedSet.remove(1); // Removes 1 from the set, returns true. Set now contains [2].
randomizedSet.insert(2); // 2 was already in the set, so return false.
randomizedSet.getRandom(); // Since 2 is the only number in the set, getRandom() will always return 2.
 

Constraints:

-231 <= val <= 231 - 1
At most 2 * 105 calls will be made to insert, remove, and getRandom.
There will be at least one element in the data structure when getRandom is called."""

import random
from random import choice

class RandomizedSet:

    def __init__(self):
        self.hash_map = {}
        self.array = []
        

    def insert(self, val: int) -> bool:
        if val in self.hash_map: return False
        
        self.hash_map[val] = len(self.array)
        self.array.append(val)
        return True
            
    def remove(self, val: int) -> bool:
        if val not in self.hash_map: return False
        
        last_element_in_list = self.array[-1]
        index_of_element_to_be_removed = self.hash_map[val]
    
        self.hash_map[last_element_in_list] = index_of_element_to_be_removed
        
        self.array[-1], self.array[index_of_element_to_be_removed] = self.array[index_of_element_to_be_removed], self.array[-1]
        
        #print(self.hash_map, self.array)
        
        self.array.pop()    
        del self.hash_map[val]
        return True

    def getRandom(self) -> int:
        return random.choice(self.array)
        


# Your RandomizedSet object will be instantiated and called as such:
obj = RandomizedSet()
param_1 = obj.insert(1)
param_2 = obj.remove(1)
param_1 = obj.insert(2)
param_3 = obj.getRandom()
print(param_3)