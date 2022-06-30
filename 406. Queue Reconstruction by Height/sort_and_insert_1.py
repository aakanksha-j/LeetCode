class Solution:
    def reconstructQueue(self, people: List[List[int]]) -> List[List[int]]:
        # leetcode solution

        # time complexity: O(n^2), O(n log n) to sort the list, O(n) for for loop on people, inside for loop
        #                  we insert n times in worst case, therefore O(n*n) = O(n^2) time
        # space complexity: O(n) for output list


        output = []

        # sort list 1. by height in reverse order and then 2. by k in ascending order
        people.sort(key = lambda x: (-x[0], x[1]))

        # insert at place specified in k
        for p in people:
            output.insert(p[1], p)

        return output
