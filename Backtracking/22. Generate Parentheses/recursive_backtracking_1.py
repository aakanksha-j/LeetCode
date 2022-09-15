class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        # leetcode solution
        # time complexity: O(2^(2n)) - n pairs of left parentheses and n pairs
        # of right parentheses, therefore 2n pairs. It becomes a recursive call
        # binary tree. Binary tree has time complexity of 2^N wherein N is the
        # height and number of nodes at every height is 2^height.
        # So here 2 parentheses, therefore 2^N nodes in that tree.
        # In 37. letterCombinations of phone number, 4 digits for 7 and 9,
        # so 4^N combinations of recursive call binary tree.

# https://leetcode.com/discuss/general-discussion/318680/backtracking-time-complexity-analysis-how-do-you-calculate
        res = []

        def dfs_backtrack(left = 0, right = 0, output = []):
            if len(output) == 2 * n:
                res.append(''.join(output))
                return

            # no for loop needed, simple recursion of base case and regenerative cases
            if left < n:
                output.append('(')
                print(output)
                dfs_backtrack(left + 1, right, output)
                output.pop()

            if right < left: # not n, but left so that sequence is always valid
                output.append(')')
                print(output)
                dfs_backtrack(left, right + 1, output)
                output.pop()

        dfs_backtrack()

        return res
