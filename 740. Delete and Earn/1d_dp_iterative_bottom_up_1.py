from collections import Counter
class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:
        # similar to house robber 1D DP iterative bottom up solution
        
        # convert given data into freq Counter
        # sort the keys of dictionary
        # run for loop on sorted keys 
        # calculate dp value for every key using last_to_last and last 
        # return last value
        
        # time: O(nlogn) because of sorted function, iterating over elements takes O(n) time
        # space: O(n) for dictionary
        
        freq = Counter()
        for num in nums:
            freq[num] += 1
        keys = sorted(freq.keys())
        last_to_last, last = 0, keys[0] * freq[keys[0]]
        for i in range(1, len(keys)):
            # key, value = keys[i], freq[keys[i]]
            if keys[i] - keys[i - 1] == 1: # adjacent elements not to be considered
                last_to_last, last = last, max(last_to_last + (keys[i] * freq[keys[i]]), last)
            else: # no need to worry about adjacent deletions
                last_to_last, last = last, last + (keys[i] * freq[keys[i]]) 
        return last


# other approach is 

from collections import Counter
class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:
        # 1D DP bottom up iterative solution 
        
        
        # create buckets array based on frequency of each element
        # [2, 20, 20, 20, 21, 1950] buckets = [2, 60, 21, 1950]
        # this way, we won't need freq Counter and sorted for keys and remembering if 2 elements are adjacent
        
        n = max(nums)
        buckets = [0] * (n + 1) # prev = 0, curr = nums[i], no need to create prev separately, buckets[0] will be prev
        for num in nums:
            buckets[num] += num # for 3 times 20 in nums, multiply need 
        #print(buckets)
        dp = [0] * (n + 1)
        dp[1] = buckets[1]
        for i in range(2, n + 1):
            dp[i] = max(dp[i - 1], dp[i - 2] + buckets[i])
        #print(dp)
        return dp[-1]
        
        
        
        