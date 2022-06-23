class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        # neetcode solution for 77 Combinations and 47 Permutations 2

        # time: n.n! - n for iterating nums, nPk = n! for permutations formula,
        # space: 3n ~ n for hashmap, recursion stack, perm copy
        #        n.n! if we take into account the space needed to store output

        def dfs_backtrack():

            if len(perm) == len(nums):
                res.append(perm.copy())
                return

            for n in nums:
            # search in array nums instead of dictionary, as it is faster and no repetitive elements
            # in permutations 2, search in dictionary because we have to keep checking until count 0
                if count[n] > 0:
                    # add
                    perm.append(n)
                    count[n] -= 1

                    dfs_backtrack()

                    # remove
                    perm.pop()
                    count[n] += 1


        res, perm = [], []

        count = {n: 0 for n in nums}
        for n in nums:
            count[n] += 1

        dfs_backtrack()

        return res
