"""# approach 1: Cascading - has time and space complexity of N.2^N. Therefore,
used backtracking method.
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        output = [[]]

        for num in nums:
            print(output)
            output += [curr + [num]  for curr in output]
            print(output)

        return output"""

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        # solution based on 90 subsets 2 - own approach

        # time complexity: O(N.2^N) - N for length of subset, 2^N to keep or skip nums[i]
        # space complexity: O(N) for recursion call stack
        
        res = []

        def rec_backtrack(start = 0, subset = []):

            # no condition needed for base case like 77 combinations as we want all combinations of given length upto n
            res.append(subset.copy())

            # for loop iterating over len(nums) not n
            for i in range(start, len(nums)):
                subset.append(nums[i]) # add
                rec_backtrack(i + 1, subset) # backtrack
                subset.pop() # remove

        rec_backtrack()

        return res
