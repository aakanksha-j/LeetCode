class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        # own Solution

        # time complexity: O(N.(4^N)) - N digits, therefore N to build the
        # combination, in general N.M^N, here M is 4 as 7 and 9 digits have
        # 4 digits.
        # space complexity: O(N) for recursion call stack, O(1) for dictionary
        # as the hashmap does not grow with input

        # instead of list, we can use a string for values
        dic = {2: ['a','b','c'], \
               3: ['d','e','f'], \
               4: ['g','h','i'], \
               5: ['j','k','l'], \
               6: ['m','n','o'], \
               7: ['p','q','r','s'] \
               8: ['t','u','v'] \
               9: ['w','x','y','z']}

        res = []


        def dfs_backtrack(output = ''):
            for digit in digits:
                for ch in digits[digit]:
                    output.append(ch) # add
                    dfs_backtrack(output) # backtrack next element
                    res.append(output) # remove

        dfs_backtrack()

        return res
