class Solution:
    def countBadPairs(self, nums: List[int]) -> int:
        # https://leetcode.com/problems/count-number-of-bad-pairs/discuss/2388183/n*(n-1)2-Valid-oror-(C%2B%2BJava)

        # count_pairs is cumulative sum of total pairs until now - good pairs
        hashmap = {}
        count_pairs = 0
        for i in range(len(nums)):
            prev = hashmap.get((i - nums[i]), 0)
            count_pairs += i - prev
            hashmap[i - nums[i]] = hashmap.get((i - nums[i]), 0) + 1

        # print(hashmap)
        return count_pairs

9 8 2022 2364 Count Number of Bad Pairs

time: O(N)
space: O(N)
create hashmap with key as difference between index and its values,
count = prev_count + index - prev, prev is count of good pairs,
whenever a good pair is found, we will subtract it from total number
of pairs to get no. of bad pairs.
