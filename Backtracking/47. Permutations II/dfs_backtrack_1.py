class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:

        # use hash map to store count of each number
        # append every element based on count
        # backtrack and remove, increase count
        # similar to 46 permutations and 77 combinations problem

        # time: n.n! - n for iterating nums, nPk = n! for permutations formula
        # space: 3n ~ n for hashmap, recursion stack, perm copy
        #        n.n! if we take into account the space needed to store output

        def dfs_backtrack():
            # base case
            if len(perm) == len(nums):
                res.append(perm.copy())
                return

            for num in count:
            # search in array nums instead of dictionary, as it is faster and no repetitive elements
            # in permutations 2, search in dictionary because we have to keep checking until count 0
                if count[num] > 0:
                    # add
                    count[num] -= 1
                    perm.append(num)

                    # backtrack
                    dfs_backtrack()

                    # remove
                    count[num] += 1
                    perm.pop()


        res, perm = [], []

        count = {num: 0 for num in nums}
        for num in nums:
            count[num] += 1

        dfs_backtrack()

        return res
