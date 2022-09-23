class Solution:
    def candy(self, ratings: List[int]) -> int:
        # https://leetcode.com/problems/candy/discuss/42769/A-simple-solution
        
        # time: O(N) go through every element 2 times
        # space: O(N) for candy array to store count
        
        """
        1 3 2 -> rating
        1 1 1 -> give 1 to all

        1 2 1 -> loop from Left to Right ( 1 to < n) if( rating[i] > rating[i-1]) add 1 to rating[i]

        1 2 1 -> loop from Right to left (from n to 0) if rating(i-1) > rating(i) , take Math.max(rating[i] +1 , rating[1-1] )

        So total = 4.
        """
        candy_array = [1] * len(ratings)
        for i in range(1, len(ratings)):
            if ratings[i] > ratings[i - 1]:
                candy_array[i] = candy_array[i - 1] + 1
        for i in range((len(ratings) - 1), 0, -1):
            if ratings[i - 1] > ratings[i]:
                candy_array[i - 1] = max(candy_array[i] + 1, candy_array[i - 1])
        output = sum(candy_array)
        return output